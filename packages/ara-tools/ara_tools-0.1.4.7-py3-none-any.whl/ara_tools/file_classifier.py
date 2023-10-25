from .classifier import Classifier

class FileClassifier:
    def __init__(self, file_system):
        self.file_system = file_system
    
    def classify_files(self, tag=None):
        files_by_classifier = {classifier: [] for classifier in Classifier.ordered_classifiers()}

        for root, _, files in self.file_system.walk("."):
            for file in files:
                file_path = self.file_system.path.join(root, file)
                if tag:
                    # Check if file contains the tag
                    with open(file_path, 'r') as f:
                        content = f.read()
                        if tag not in content:
                            continue
                
                for classifier in Classifier.ordered_classifiers():
                    if file.endswith(f".{classifier}"):
                        files_by_classifier[classifier].append(file_path)
        return files_by_classifier
    
    def print_classified_files(self, files_by_classifier):
        for classifier, files in files_by_classifier.items():
            if files:
                print(f"{classifier.capitalize()} files:")
                for file in files:
                    print(f"  - {file}")
                print()
