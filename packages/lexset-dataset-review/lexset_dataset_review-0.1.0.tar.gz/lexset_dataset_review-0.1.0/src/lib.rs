use pyo3::prelude::*;

#[pyfunction]
fn adaptive_histogram_matching(synthetic_dir: String, real_dir: String, output_dir: String) -> PyResult<()> {
    Python::with_gil(|py| {
        let py_code = format!(
            r#"
import os
import cv2
import numpy as np

def adaptive_histogram_matching_for_images(synthetic_dir, real_dir, output_dir):

    def adjust_brightness(source_img, target_img):
        # Convert images to HSV
        source_hsv = cv2.cvtColor(source_img, cv2.COLOR_BGR2HSV)
        target_hsv = cv2.cvtColor(target_img, cv2.COLOR_BGR2HSV)

        # Calculate average brightness (V channel) of target image
        target_v_avg = np.mean(target_hsv[:,:,2])

        # Calculate average brightness (V channel) of source image
        source_v_avg = np.mean(source_hsv[:,:,2])

        # Calculate the scale factor for brightness
        scale_factor_v = target_v_avg / source_v_avg

        # Calculate average of color (S channel) of target image
        target_s_avg = np.mean(target_hsv[:,:,1])

        # Calculate average of color (S channel) of source image
        source_s_avg = np.mean(source_hsv[:,:,1])

        # Calculate the scale factor for color
        scale_factor_s = target_s_avg / source_s_avg

        # Apply scale factor to the V and S channels of source image
        source_hsv[:,:,2] = np.clip(source_hsv[:,:,2] * scale_factor_v, 0, 255).astype(np.uint8)
        source_hsv[:,:,1] = np.clip(source_hsv[:,:,1] * scale_factor_s, 0, 255).astype(np.uint8)

        # Convert the source image back to BGR color space
        adjusted_img = cv2.cvtColor(source_hsv, cv2.COLOR_HSV2BGR)
        return adjusted_img

    synthetic_images = os.listdir(synthetic_dir)
    real_images = os.listdir(real_dir)

    # Define the CLAHE parameters
    clip_limit = 0.5  # Threshold for contrast limiting
    grid_size = (8, 8)  # Size of the grid for histogram equalization

    for idx, synthetic_image in enumerate(synthetic_images):
        synthetic_image_path = os.path.join(synthetic_dir, synthetic_image)
        synthetic_img = cv2.imread(synthetic_image_path, cv2.IMREAD_COLOR)

        real_image_path = os.path.join(real_dir, real_images[idx % len(real_images)])
        real_img = cv2.imread(real_image_path, cv2.IMREAD_COLOR)

        # Convert the images to LAB color space for better contrast manipulation
        synthetic_lab = cv2.cvtColor(synthetic_img, cv2.COLOR_BGR2Lab)
        real_lab = cv2.cvtColor(real_img, cv2.COLOR_BGR2Lab)

        # Split the LAB images into separate channels
        synthetic_l, synthetic_a, synthetic_b = cv2.split(synthetic_lab)
        real_l, real_a, real_b = cv2.split(real_lab)

        # Apply CLAHE to the L channel
        clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=grid_size)
        matched_l = clahe.apply(synthetic_l)

        # Merge the CLAHE-enhanced L channel with the original A and B channels
        matched_lab = cv2.merge((matched_l, synthetic_a, synthetic_b))

        # Convert the matched LAB image back to BGR color space
        matched_img = cv2.cvtColor(matched_lab, cv2.COLOR_Lab2BGR)

        # Adjust the brightness to match the real image
        adjusted_img = adjust_brightness(matched_img, real_img)

        output_path = os.path.join(output_dir, synthetic_image)
        cv2.imwrite(output_path, adjusted_img)

synthetic_dir = "{}"
real_dir = "{}"
output_dir = "{}"
    
adaptive_histogram_matching_for_images(synthetic_dir, real_dir, output_dir)
    
"#,
            synthetic_dir, real_dir, output_dir
        );

        let res = py.run(&py_code, None, None);
        match res {
            Ok(_) => println!("Color transfer executed successfully."),
            Err(e) => e.print_and_set_sys_last_vars(py),
        }
    });
    
    Ok(())
}

#[pyfunction]
fn color_transfer_mean(synthetic_dir: String, real_dir: String, output_dir: String) -> PyResult<()> {
    Python::with_gil(|py| {
        let py_code = format!(
            r#"
import os
import cv2
import numpy as np

from concurrent.futures import ThreadPoolExecutor

#good one

def color_transfer_using_mean_std(source_img, target_img):
    # Calculate mean and standard deviation of source and target images
    s_mean = np.mean(source_img, axis=(0, 1))
    s_std = np.std(source_img, axis=(0, 1))
    t_mean = np.mean(target_img, axis=(0, 1))
    t_std = np.std(target_img, axis=(0, 1))

    # Transfer color
    result = ((source_img - s_mean) * (t_std / s_std)) + t_mean

    # Clip to valid color range and round to integer
    result = np.around(np.clip(result, 0, 255)).astype(np.uint8)

    return result


def color_transfer_for_images(synthetic_dir, real_dir, output_dir):
    synthetic_images = [img for img in os.listdir(synthetic_dir) if 'rgb' in img.lower()]  # Only get images with "rgb" in their filename
    real_images = os.listdir(real_dir)
    
    def process_image(idx):
        synthetic_image = synthetic_images[idx]
        synthetic_image_path = os.path.join(synthetic_dir, synthetic_image)
        synthetic_img = cv2.imread(synthetic_image_path, cv2.IMREAD_COLOR)

        real_image_path = os.path.join(real_dir, real_images[idx % len(real_images)])
        real_img = cv2.imread(real_image_path, cv2.IMREAD_COLOR)

        matched_img = color_transfer_using_mean_std(synthetic_img, real_img)

        output_path = os.path.join(output_dir, synthetic_image)
        cv2.imwrite(output_path, matched_img)
        
    with ThreadPoolExecutor() as executor:
        executor.map(process_image, range(len(synthetic_images)))
            
synthetic_dir = "{}"
real_dir = "{}"
output_dir = "{}"
    
color_transfer_for_images(synthetic_data_dir, real_data_dir, output_data_dir)
    
"#,
            synthetic_dir, real_dir, output_dir
        );

        let res = py.run(&py_code, None, None);
        match res {
            Ok(_) => println!("Color transfer executed successfully."),
            Err(e) => e.print_and_set_sys_last_vars(py),
        }
    });
    
    Ok(())
}


#[pyfunction]
fn transfer_shot_noise(synthetic_dir: String, real_dir: String, output_dir: String) -> PyResult<()> {
    Python::with_gil(|py| {
        let py_code = format!(
            r#"
import os
import numpy as np
from PIL import Image
import random

def apply_shot_noise_to_synthetic(real_image_directory, synthetic_directory, output_directory):
    synthetic_shape = (0, 0)
    synthetic_images = [fname for fname in os.listdir(synthetic_directory) if fname.lower().endswith('.bmp')]
    if synthetic_images:
        first_synthetic_image = Image.open(os.path.join(synthetic_directory, synthetic_images[0]))
        synthetic_shape = first_synthetic_image.size

    real_images = [os.path.join(real_image_directory, f) for f in os.listdir(real_image_directory) if f.lower().endswith('.bmp')]

    # Compute real_image_mean
    all_images = []
    for image_name in os.listdir(real_image_directory):
        if image_name.endswith(".bmp"):
            image_path = os.path.join(real_image_directory, image_name)
            image = Image.open(image_path).resize(synthetic_shape, Image.LANCZOS)
            all_images.append(np.array(image))

    real_img_mean = np.mean(all_images, axis=0)

    for synthetic_image_path in synthetic_images:
        output_image_path = os.path.join(output_directory, os.path.basename(synthetic_image_path))
        synthetic_img = np.array(Image.open(os.path.join(synthetic_directory, synthetic_image_path)))

        # Randomly select a real image
        real_image_path = random.choice(real_images)
        real_img = Image.open(real_image_path)
        real_img = real_img.resize(synthetic_shape)
        real_img = np.array(real_img)

        # Adjust noise
        poisson_real_img = np.random.poisson(real_img)
        shot_noise = real_img - poisson_real_img
        noisy_synthetic_img = synthetic_img + shot_noise
        noisy_synthetic_img = np.clip(noisy_synthetic_img, 0, 255).astype(np.uint8)

        Image.fromarray(noisy_synthetic_img).save(output_image_path)

synthetic_dir = "{}"
real_dir = "{}"
output_dir = "{}"
    
apply_shot_noise_to_synthetic(real_data_dir,synthetic_data_dir,output_data_dir)
    
"#,
            synthetic_dir, real_dir, output_dir
        );

        let res = py.run(&py_code, None, None);
        match res {
            Ok(_) => println!("Noise transfer executed successfully."),
            Err(e) => e.print_and_set_sys_last_vars(py),
        }
    });
    
    Ok(())
}

/// A Python module implemented in Rust.
#[pymodule]
fn lexset_dataset_review(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(adaptive_histogram_matching, m)?)?;
    m.add_function(wrap_pyfunction!(color_transfer_mean, m)?)?;
    m.add_function(wrap_pyfunction!(transfer_shot_noise, m)?)?;
    Ok(())
}