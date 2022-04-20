# Data Lineage Visualization

This python application helps to convert textual information of dataflow or routes between points or any other lineage information into a graphical/tree representation.

## Input Data Feed
  * This application is built to take csv file as input with all the dataflow information
  * This can be extended further into other file types or database tables
  
  **Sample Input:**
  
  ![image](https://user-images.githubusercontent.com/47193369/164220554-53ccc140-d83e-4bf1-8e83-02a377c30a25.png)


## Output:
  This application will generate a HTML output of the lineage/route graph
  
 **Sample Output:**
  
  ![image](https://user-images.githubusercontent.com/47193369/164220966-108c427c-d6aa-48cc-8dbe-1ffa6c9f73a2.png)

## Future Enhancements:
* Dynamic Number of Nodes in each brach (Currently static 4)
* Desired Output File Types (Currently HTML)
* Desired Shapes (Currently hardcode dot)
