# Cat-Dog Classifier

Welcome to the **Cat-Dog Classifier** project! This project is designed to classify images into two categories: cats and dogs. The workflow is modular, ensuring ease of development, debugging, and deployment.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Project Workflows](#project-workflows)
- [File Descriptions](#file-descriptions)
- [How to Run](#how-to-run)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The **Cat-Dog Classifier** project uses machine learning techniques to identify whether an input image contains a cat or a dog. The system is designed to achieve high accuracy and adaptability while maintaining a modular structure for scalability and ease of maintenance.

## Features

- **Image Classification**: Classifies images into two categories: cats and dogs.
- **Modular Design**: Well-organized project structure with reusable components.
- **Configurable Parameters**: Flexible configurations through YAML files.
- **Scalable Pipelines**: Easily extendable pipeline for adding new features.

## Technologies Used

- **Programming Language**: Python
- **Frameworks and Libraries**: TensorFlow/PyTorch, OpenCV, NumPy, Pandas, Matplotlib
- **Configuration Management**: YAML
- **Version Control**: Git

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/saurav-sabu/Cat-Dog-Classifier.git
   cd cat-dog-classifier
   ```

2. Set up a virtual environment:
   ```bash
   conda create -p venv python=3.10 -y
   conda activate venv/  
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure project settings by updating the following YAML files:
   - `config.yaml`
   - `secrets.yaml` (optional)
   - `params.yaml`

5. Prepare the dataset and ensure it is in the specified format.

## Project Workflows

Follow the steps below to build and run the project:

1. **Update `config.yaml`**: Define project-level configurations, such as paths and general settings.
2. **Update `secrets.yaml` [Optional]**: Specify sensitive data (e.g., API keys).
3. **Update `params.yaml`**: Adjust hyperparameters like learning rate, batch size, epochs, etc.
4. **Update the Entity**: Define data classes to standardize the structure of your inputs and outputs.
5. **Update the Configuration Manager in `src/config`**: Implement methods to read and manage configurations.
6. **Update the Components**: Build or modify components for data preprocessing, model training, and evaluation.
7. **Update the Pipeline**: Assemble components to create a seamless pipeline for training and inference.
8. **Update `main.py`**: Serve as the entry point to execute the pipeline.

## File Descriptions

- `config.yaml`: Project-level configuration settings.
- `secrets.yaml`: Optional file for storing sensitive information securely.
- `params.yaml`: Hyperparameters and model-specific configurations.
- `src/`: Contains source code, including configuration management, components, and pipeline logic.
- `main.py`: Entry point to execute the project.
- `requirements.txt`: List of required Python packages.
- `README.md`: Project documentation.

## How to Run

1. Activate the virtual environment:
   ```bash
   conda activate venv/
   ```

2. Execute the project:
   ```bash
   python main.py
   ```

3. Monitor the output logs and check the results.

## Contributing

We welcome contributions to the **Cat-Dog Classifier** project. Please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of your changes"
   ```
4. Push the changes and create a pull request.

## License

This project is licensed under the Apache-2.0 license. See the `LICENSE` file for more details.

---

Happy Coding! 🐱🐶

