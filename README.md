<br/>
<p align="center">
  <h3 align="center">Wholesale Customer Segmentation Through Mean Shift Clustering</h3>

  <p align="center">
    Transform your wholesale strategy with data-driven clustering insights!
    <br/>
    <br/>
  </p>
</p>

![Downloads](https://img.shields.io/github/downloads/TribeOfJudahLion/MeanShift-Clustering-Visualization-For-Wholesale-Customer-Segmentation/total) ![Contributors](https://img.shields.io/github/contributors/TribeOfJudahLion/MeanShift-Clustering-Visualization-For-Wholesale-Customer-Segmentation?color=dark-green) ![Issues](https://img.shields.io/github/issues/TribeOfJudahLion/MeanShift-Clustering-Visualization-For-Wholesale-Customer-Segmentation) ![License](https://img.shields.io/github/license/TribeOfJudahLion/MeanShift-Clustering-Visualization-For-Wholesale-Customer-Segmentation) 

## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
* [Contributing](#contributing)
* [License](#license)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

## About The Project

### Problem Scenario:

**Background**: A wholesale distributor is looking to optimize their delivery process for various products such as Fresh produce, Milk, Grocery items, Frozen goods, Detergents, and Delicatessen. The distributor has a diverse customer base, including small cafes, large restaurants, retail shops, and big-box stores. The challenge is to understand the buying patterns of these customers to improve the efficiency of the supply chain and customize services for different customer segments.

**Problem**: The distributor's current delivery system is not tailored to the specific needs of different customer segments, leading to inefficiencies such as increased delivery costs, wasted perishable goods, and customer dissatisfaction due to a one-size-fits-all approach.

**Objective**: To segment the customer base into distinct groups with similar purchasing behaviors, enabling the distributor to customize delivery schedules, optimize inventory management, and enhance customer satisfaction.

### Solution Using the Provided Code:

1. **Data Collection and Preparation**:
   - The distributor compiles historical purchase data into a CSV file (`wholesale.csv`), with each row representing a different customer and columns for different product categories.

2. **Data Loading**:
   - Using the `load_data(file_path)` function, the script reads the CSV file into a DataFrame, handling any potential errors (e.g., file not found or corrupted data).

3. **Clustering Analysis**:
   - The `perform_clustering(X)` function is used to apply the MeanShift algorithm on the data, determining the natural groupings (clusters) within the customers based on their purchase patterns.
   - The `estimate_bandwidth` function determines the bandwidth parameter for the MeanShift algorithm, which is crucial for identifying the clusters' size and location in the feature space.
   - The `MeanShift` algorithm is executed with the estimated bandwidth and `bin_seeding` for efficiency.

4. **Result Interpretation**:
   - The clustering process outputs labels for each customer, indicating their cluster membership, and the coordinates of each cluster's centroid, representing the average purchase behavior of the segment.
   - The script then prints the number of clusters and the centroids, providing a clear profile of each customer segment.

5. **Visualization**:
   - The `plot_clusters(centroids, names)` function generates a scatter plot, mapping the centroids of the clusters in a 2D space, typically representing two key product categories for clarity, such as Milk and Groceries.
   - This visualization aids in understanding the distribution and central tendency of each cluster, which is vital for strategic planning.

6. **Strategic Business Actions**:
   - Based on the clusters, the distributor can now create tailored strategies, such as:
     - **Custom Delivery Schedules**: Align delivery frequency with the buying patterns of each segment.
     - **Inventory Management**: Stock warehouses according to the cluster demands, reducing waste of perishables.
     - **Targeted Marketing**: Develop marketing campaigns that appeal to the specific needs and purchasing behaviors of each cluster.
     - **Pricing Strategies**: Adjust pricing based on the volume and frequency of orders from each segment.
   
7. **Continuous Improvement**:
   - Over time, the distributor can re-run the analysis periodically to capture changes in customer buying behaviors, ensuring that the delivery system remains optimized.

By leveraging the MeanShift clustering algorithm and the historical purchase data, the wholesale distributor can efficiently segment their customer base, leading to improved logistics, cost savings, and enhanced customer service.

The script is a Python program designed for clustering analysis using the MeanShift algorithm, commonly applied in machine learning for unsupervised data categorization. 

1. **Importing Necessary Libraries:**
   - `pandas`: A powerful data manipulation and analysis library.
   - `numpy`: A fundamental package for scientific computing with Python.
   - `MeanShift`, `estimate_bandwidth`: From `sklearn.cluster`, these are used for clustering based on MeanShift algorithm.
   - `matplotlib.pyplot`: A plotting library for creating static, animated, and interactive visualizations.

2. **Function `load_data(file_path)`**:
   - **Purpose**: To load data from a CSV file.
   - **Inputs**: `file_path` - the path to the CSV file.
   - **Process**: It attempts to read the CSV file using `pandas.read_csv()`.
   - **Error Handling**: If an error occurs during file reading (e.g., file not found, invalid format), it prints an error message and returns `None`.
   - **Outputs**: A DataFrame containing the loaded data.

3. **Function `perform_clustering(X)`**:
   - **Purpose**: To perform clustering on the dataset.
   - **Inputs**: `X` - a numpy array of data points.
   - **Process**:
     - `estimate_bandwidth`: Estimates the bandwidth to use with the MeanShift algorithm.
     - `MeanShift`: Performs clustering with the estimated bandwidth. `bin_seeding` is set to `True` for computational efficiency.
   - **Outputs**: Returns two elements:
     - `labels_`: Labels of each point.
     - `cluster_centers_`: Coordinates of the cluster centers.

4. **Function `plot_clusters(centroids, names)`**:
   - **Purpose**: To plot the centroids of the clusters.
   - **Inputs**:
     - `centroids`: The coordinates of the cluster centers.
     - `names`: Column names of the data, used for labeling axes.
   - **Process**: 
     - Uses `matplotlib` to plot a scatter plot of centroids.
     - Each centroid is annotated with its cluster number.
   - **Visualization**: The plot is customized with labels, title, and grid.

5. **Main Program Execution (`main()` function)**:
   - **Data Loading**: Loads the data from 'wholesale.csv' using `load_data`.
   - **Clustering**:
     - If data is successfully loaded, it extracts the relevant columns for clustering (`X`).
     - Calls `perform_clustering` to get cluster labels and centroids.
     - Prints the number of clusters and the centroids' coordinates.
   - **Plotting**: Calls `plot_clusters` to visualize the centroids.

6. **Entry Point**: If the script is executed as the main program (`if __name__ == "__main__":`), it runs the `main()` function.

This script is specifically tailored for clustering analysis using the MeanShift algorithm and is designed to work with a particular data format (e.g., 'wholesale.csv'). It includes basic error handling for data loading and employs data visualization to present the results of the clustering.

The output includes both a visual plot and textual data summarizing the results of the clustering:

1. **Plot Explanation**:
   - The plot is a scatter diagram of cluster centroids obtained from the MeanShift algorithm.
   - The x-axis and y-axis likely represent two of the features from the dataset (e.g., 'Region' and 'Fresh'). However, without specific axis labels from the code, the exact features they represent are assumed based on the plot's title.
   - Each point on the plot is a centroid of a cluster.
   - There are annotations near each point labeling the cluster numbers from 0 to 7, indicating that eight clusters have been found in the data.

2. **Textual Output Explanation**:
   - The script prints out the number of clusters found in the input data, which is 8.
   - It then prints the centroids of these clusters.
   - The labels `Fre`, `Mil`, `Gro`, `Fro`, `Det`, `Del` are likely shorthand for the features in the dataset such as Fresh, Milk, Grocery, Frozen, Detergents_Paper, Delicatessen respectively.
   - Each row after the labels represents the centroid of a cluster. For instance, the first centroid has coordinates (`9632`, `4671`, `6593`, `2570`, `2296`, `1248`), which means for this cluster, the average 'Fresh' value is 9632, the average 'Milk' value is 4671, and so on for the other features.

3. **Conclusion from Results**:
   - The eight clusters suggest that the dataset can be segmented into eight different groups based on the purchasing patterns of the wholesale customers.
   - Each centroid represents the "average" customer in that cluster, with the values providing a profile of what those customers typically buy.
   - For example, Cluster 7 seems to spend a lot on 'Grocery' and 'Detergents_Paper', which may indicate large retail stores, whereas Cluster 0 has lower values across the board, which might indicate smaller outlets or markets.

4. **Implications for Business**:
   - These insights can help a wholesaler understand the different types of customers they serve.
   - The wholesaler could tailor their marketing, inventory, and delivery strategies to better meet the needs of each cluster of customers.

This detailed analysis of the cluster centroids and the scatter plot visualization is a key output of unsupervised learning tasks in data science, providing valuable insights for strategic decision-making in businesses.

## Built With

#### Languages and Tools:

- **Python**: The primary programming language used for writing the script. Python is chosen for its vast ecosystem of data science libraries and ease of writing readable code.

#### Libraries:

- **Pandas**: Utilized for data manipulation and analysis. It offers data structures and operations for manipulating numerical tables and time series, making it perfect for handling and processing structured data.

- **NumPy**: A fundamental package for scientific computing in Python. It provides support for arrays (beyond the capabilities of Python's built-in lists), along with a host of functions for performing operations on these arrays. It's especially useful for handling large multi-dimensional arrays and matrices.

- **scikit-learn (Sklearn)**: An open-source machine learning library for Python. It features various classification, regression, and clustering algorithms including k-means, random forests, gradient boosting, k-nearest neighbors, and this project specifically uses:
  - `MeanShift`: For clustering, it is a non-parametric feature-space analysis technique, a form of unsupervised learning.
  - `estimate_bandwidth`: To automatically infer the bandwidth (a parameter of the MeanShift algorithm) based on the input data.

- **Matplotlib**: A plotting library for the Python programming language and its numerical mathematics extension, NumPy. Used for creating static, interactive, and animated visualizations in Python, it's employed in this project to visualize the results of the clustering, specifically the centroids of the clusters in the data.

#### Development Environments and Tools:

- **Jupyter Notebook/PyCharm/Other IDEs**: While the specific development environment is not mentioned, this Python script can be run in various integrated development environments (IDEs) that support Python, such as Jupyter Notebook, PyCharm, VS Code, etc. These tools provide features like code linting, syntax highlighting, and debugging that aid in the development process.

#### Version Control:

- **Git**: Assumed to be used for version control, allowing for the tracking of changes, collaboration, and management of the codebase over time.

#### Platforms:

- **GitHub**: The likely platform for hosting the repository, managing the code, and documenting the project through README files and other markdown documents. It facilitates version control and collaboration.

This section of a GitHub README file would provide visitors with a quick overview of the technical stack used to build the software. It's important for developers who might want to understand what technologies they need to work with if they are considering contributing to the project.Here are a few examples.

## Getting Started

#### Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed the latest version of [Python](https://www.python.org/downloads/). This project is built with Python 3.x.
- You have a Windows, Linux, or Mac machine with permission to install packages.
- You are familiar with basic Python programming and command-line operations.

#### Installation

1. **Clone the repository**

   Start by cloning the repository to your local machine. You can do this by running the following command in your terminal or command prompt:

   ```sh
   git clone [URL to the GitHub repository]
   ```

   Replace `[URL to the GitHub repository]` with the actual repository URL.

2. **Set up a virtual environment (optional but recommended)**

   Navigate to the project directory and create a virtual environment. This will keep your dependencies organized and project-specific.

   For Unix/macOS:

   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

   For Windows:

   ```sh
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install the required packages**

   With your virtual environment activated, install the required packages using `pip`:

   ```sh
   pip install pandas numpy scikit-learn matplotlib
   ```

#### Running the Project

To run the project, follow these steps:

1. **Prepare your dataset**

   Ensure you have a CSV dataset named `wholesale.csv` with the appropriate structure for the clustering analysis. Place this file in the root directory of the project.

2. **Execute the script**

   Run the main script using Python from the terminal:

   ```sh
   python main.py
   ```

   If your dataset is named differently or located elsewhere, modify the `input_file` variable in the `main()` function accordingly.

3. **View the results**

   The script will output the number of clusters found and the centroids for each cluster in the terminal. A plot will also be displayed showing the centroids of the clusters.

#### Contributing to the Project

If you want to contribute to the project, here are some steps you should follow:

1. Create a branch for your new feature or fix:

   ```sh
   git checkout -b [branch-name]
   ```

2. Make and test your changes.

3. Commit your changes:

   ```sh
   git commit -m "Add some feature"
   ```

4. Push to the branch:

   ```sh
   git push origin [branch-name]
   ```

5. Create a new Pull Request.

Remember to update tests as appropriate, adhere to the coding standards set by the project maintainers, and update documentation if necessary.

For more detailed instructions, refer to the `CONTRIBUTING.md` file in the project repository (if available).

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com/TribeOfJudahLion/MeanShift-Clustering-Visualization-For-Wholesale-Customer-Segmentation/issues/new) to discuss it, or directly create a pull request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please also read through the [Code Of Conduct](https://github.com/TribeOfJudahLion/MeanShift-Clustering-Visualization-For-Wholesale-Customer-Segmentation/blob/main/CODE_OF_CONDUCT.md) before posting your first idea as well.

### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [LICENSE](https://github.com/TribeOfJudahLion/MeanShift-Clustering-Visualization-For-Wholesale-Customer-Segmentation/blob/main/LICENSE.md) for more information.

## Authors

* **Robbie** - *PhD Computer Science Student* - [Robbie](https://github.com/TribeOfJudahLion) - **

## Acknowledgements

* []()
* []()
* []()
