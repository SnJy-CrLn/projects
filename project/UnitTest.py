import unittest
import pandas as pd
from studentpredicton import load_data, preprocess_data, train_model, predict, evaluate_model

class TestStudentPerformancePrediction(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Load sample data
        cls.data = load_data("MINOR EXCEL SHEET.csv")  # Replace with actual path or method of loading
        cls.processed_data = preprocess_data(cls.data)
        
        # Example training split
        cls.X_train = cls.processed_data.drop('target', axis=1)
        cls.y_train = cls.processed_data['target']
        
        # Train model
        cls.model = train_model(cls.X_train, cls.y_train)
    
    def test_data_loading(self):
        """Test if the data loads correctly."""
        data = load_data("sample_data.csv")  # Replace with actual path or function name
        self.assertIsInstance(data, pd.DataFrame, "Data should be loaded as a DataFrame.")
        self.assertTrue(len(data) > 0, "Data should not be empty.")
    
    def test_data_preprocessing(self):
        """Test if the data preprocessing outputs the correct structure."""
        processed_data = preprocess_data(self.data)
        self.assertIn('target', processed_data.columns, "Processed data should contain a target column.")
        self.assertFalse(processed_data.isnull().values.any(), "Processed data should have no null values.")
    
    def test_feature_engineering(self):
        """Check if features are engineered correctly, if applicable."""
        # Example: checking if specific engineered features exist
        processed_data = preprocess_data(self.data)
        # Add specific checks here, like:
        # self.assertIn('new_feature', processed_data.columns, "Expected feature missing.")
    
    def test_model_training(self):
        """Verify that model training works and returns a valid model."""
        model = train_model(self.X_train, self.y_train)
        self.assertIsNotNone(model, "Model should be instantiated.")
        self.assertTrue(hasattr(model, 'predict'), "Model should have a predict method.")
    
    def test_model_prediction(self):
        """Check if the model makes predictions of the expected format."""
        predictions = predict(self.model, self.X_train)
        self.assertEqual(len(predictions), len(self.y_train), "Predictions length should match input length.")
        self.assertTrue(all(isinstance(pred, (int, float)) for pred in predictions), "Predictions should be numeric.")
    
    def test_model_evaluation(self):
        """Validate evaluation metrics calculation."""
        predictions = predict(self.model, self.X_train)
        results = evaluate_model(self.y_train, predictions)
        # Example: check that metrics exist in results dictionary
        self.assertIn('accuracy', results, "Results should contain accuracy metric.")
        self.assertIn('precision', results, "Results should contain precision metric.")
        self.assertIn('recall', results, "Results should contain recall metric.")
        # Check that all metrics are within a valid range (0 to 1 for probabilities, etc.)
        for metric, value in results.items():
            self.assertTrue(0 <= value <= 1, f"{metric} should be between 0 and 1.")
    
    def test_edge_cases_empty_data(self):
        """Test handling of empty input data."""
        empty_data = pd.DataFrame()
        with self.assertRaises(ValueError):
            preprocess_data(empty_data)
        
    def test_edge_cases_unseen_data(self):
        """Test handling of unseen data with possibly new categories or nulls."""
        unseen_data = self.X_train.copy()
        unseen_data.loc[0, 'new_feature'] = None  # Injecting null value
        with self.assertRaises(Exception):
            predict(self.model, unseen_data)

if __name__ == "__main__":
    unittest.main()
