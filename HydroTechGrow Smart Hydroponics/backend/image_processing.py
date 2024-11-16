import cv2

def process_plant_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    disease_detected = "Yes" if gray.mean() < 100 else "No"  # Placeholder logic
    return {
        "disease_detected": disease_detected,
        "average_intensity": gray.mean(),
    }
