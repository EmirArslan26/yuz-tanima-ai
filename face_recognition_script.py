#!/usr/bin/env python3
"""
Simple face recognition script using face_recognition and OpenCV.
Loads known faces from a directory and recognizes faces in a given image.
"""

import os
import argparse
import face_recognition
import cv2


def load_known_faces(known_dir: str):
    """Load images from known_dir and return encodings and names."""
    known_encodings = []
    known_names = []
    # Loop through files in the directory
    for filename in os.listdir(known_dir):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            filepath = os.path.join(known_dir, filename)
            # Load the image and compute face encodings
            image = face_recognition.load_image_file(filepath)
            encodings = face_recognition.face_encodings(image)
            if encodings:
                known_encodings.append(encodings[0])
                # Use filename (without extension) as the label
                name = os.path.splitext(filename)[0]
                known_names.append(name)
                print(f"Loaded encoding for {name}")
            else:
                print(f"No faces found in {filename}")
    return known_encodings, known_names


def recognize_faces(image_path: str, known_encodings, known_names, output_path: str = None):
    """Recognize faces in the given image and optionally save annotated output."""
    # Load the target image
    image = face_recognition.load_image_file(image_path)
    # Detect face locations and encodings
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)

    # Convert to BGR format for OpenCV drawing
    cv2_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    results = []
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Compare this face encoding against known encodings
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        name = "Unknown"
        if True in matches:
            # Use the first matched known face
            first_index = matches.index(True)
            name = known_names[first_index]
        results.append((name, (top, right, bottom, left)))

        # Draw rectangle and label if output path is specified
        if output_path:
            cv2.rectangle(cv2_image, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(
                cv2_image,
                name,
                (left, top - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 0),
                1,
            )

        # Print result to console
        print(
            f"Found {name}: (Top, Right, Bottom, Left) = ({top}, {right}, {bottom}, {left})"
        )

    # Save annotated image if requested
    if output_path:
        cv2.imwrite(output_path, cv2_image)
        print(f"Output image saved to {output_path}")

    return results


def main():
    parser = argparse.ArgumentParser(
        description="Simple face recognition script that compares faces in an image to known faces."
    )
    parser.add_argument(
        "--known_dir",
        required=True,
        help="Directory containing images of known people. Filenames (without extension) are used as labels.",
    )
    parser.add_argument(
        "--image",
        required=True,
        help="Path to the image file in which to recognize faces.",
    )
    parser.add_argument(
        "--output",
        help="Optional path to save an output image annotated with bounding boxes and names.",
    )
    args = parser.parse_args()

    known_encodings, known_names = load_known_faces(args.known_dir)
    if not known_encodings:
        print("No known face encodings found. Please add images to the known faces directory.")
        return

    recognize_faces(args.image, known_encodings, known_names, args.output)


if __name__ == "__main__":
    main()
