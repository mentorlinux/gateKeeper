# qr_scanner/views.py
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import threading
from .models import BusEntry
from qr_generator.models import DriverInfo
import cv2
from pyzbar.pyzbar import decode
from datetime import datetime

# Assuming `scanned_data` is a global variable in this module
scanned_data = []  # This stores scanned QR code details
lock = threading.Lock()  # Lock for thread-safe operations

def get_scanned_qr_codes(request):
    """Return the scanned QR codes as JSON."""
    with lock:  # Ensure thread-safe access to `scanned_data`
        return JsonResponse(scanned_data, safe=False)
    
def scan_qr_code(request):
    # Initialize camera
    cap = cv2.VideoCapture(0)
    scanned_buses = set()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        decoded_objects = decode(frame)
        for obj in decoded_objects:
            bus_number = obj.data.decode('utf-8')

            if bus_number not in scanned_buses:
                # Check if the bus exists
                try:
                    driver_info = DriverInfo.objects.get(bus_number=bus_number)
                    BusEntry.objects.create(
                        bus_number=bus_number,
                        driver_name=driver_info.driver_name,
                        driver_number=driver_info.driver_number,
                    )
                    scanned_buses.add(bus_number)
                except DriverInfo.DoesNotExist:
                    print(f"Bus number {bus_number} not found in database!")

        # Display the camera feed
        cv2.imshow("QR Code Scanner", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
            break

    cap.release()
    cv2.destroyAllWindows()
    return HttpResponse("Scanning completed!")
