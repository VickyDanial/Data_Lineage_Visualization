"""This is a python application to visualize data lineage"""
import os

from pyvis.network import Network
import pandas as pd


class NoDataLineage(Exception):
    """
    Simple Class to handle data lineage Issue
    """
    pass


def read_user_input(file_nm, filter_col_nm, filter_col_val):
    df = pd.read_csv(file_nm, keep_default_na=False, dtype=str)
    visual_df = df[df[filter_col_nm] == filter_col_val]
    return visual_df


def main():
    filter_col_nm='table_name'
    filter_table='customer'
    file_name=os.path.join(os.getcwd(), 'lineage_input_dataset.csv')

    # Configurations/Initializations
    color_codes_ref = ["#3E7DCC", "#8F9CB3", "00C8C8", "#F9D84A", "#8CC0FA", "4D525A", "3E7DCC"]
    y_node_len = 50
    x_node_len = 100
    x_start = -200
    y_start = 0

    visual_df = read_user_input(file_name, filter_col_nm, filter_table)
    total_branches = len(visual_df)
    if total_branches < 1:
        raise NoDataLineage

    # y_start based on total branches
    if total_branches % 2 == 1:
        y_start = (total_branches//2)*y_node_len*-1
    else:
        y_start = (((total_branches//2)*y_node_len)-(y_node_len/2))*-1

    # Initializing Root Node Data
    temp_nodes_ids = [1]
    temp_nodes_labels = [filter_table]
    temp_nodes_edges = []
    temp_y_coordinates = [0]
    temp_x_coordinates = [-200]
    temp_nodes_colors = [color_codes_ref[0]]

    branch_id=2 # starts from 2 as 1 is assigned to root
    # initializing child nodes & edges based on input data
    for indx, record in visual_df.iterrows():
        prev_id = 1 # initializing with root_id
        x_start = -200
        if record[1].strip() != '':  # can use record.col_nm for static columns
            x_start += x_node_len
            curr_id = branch_id
            temp_nodes_ids.append(curr_id)
            temp_nodes_labels.append(record[1])
            temp_nodes_edges.append((prev_id,curr_id))
            temp_x_coordinates.append(x_start)
            temp_y_coordinates.append(y_start)
            temp_nodes_colors.append(color_codes_ref[1])
            prev_id = branch_id
        if record[2].strip() != '':
            x_start += x_node_len
            curr_id = (branch_id*10)+1
            temp_nodes_ids.append(curr_id)
            temp_nodes_labels.append(record[2])
            temp_nodes_edges.append((prev_id, curr_id))
            temp_x_coordinates.append(x_start)
            temp_y_coordinates.append(y_start)
            temp_nodes_colors.append(color_codes_ref[2])
            prev_id = curr_id
        if record[3].strip() != '':
            x_start += x_node_len
            curr_id = (branch_id*10)+2
            temp_nodes_ids.append(curr_id)
            temp_nodes_labels.append(record[3])
            temp_nodes_edges.append((prev_id, curr_id))
            temp_x_coordinates.append(x_start)
            temp_y_coordinates.append(y_start)
            temp_nodes_colors.append(color_codes_ref[3])
            prev_id = curr_id
        if record[4].strip() != '':
            x_start += x_node_len
            curr_id = (branch_id*10)+3
            temp_nodes_ids.append(curr_id)
            temp_nodes_labels.append(record[4])
            temp_nodes_edges.append((prev_id, curr_id))
            temp_x_coordinates.append(x_start)
            temp_y_coordinates.append(y_start)
            temp_nodes_colors.append(color_codes_ref[4])
            prev_id = curr_id
        branch_id += 1
        y_start += y_node_len

    # creating network instance
    data_lineage = Network(directed=True, height="300px", width="800px")
    for i in range(len(temp_nodes_ids)):
        data_lineage.add_node(n_id=temp_nodes_ids[i],
                              label=temp_nodes_labels[i],
                              color=temp_nodes_colors[i],
                              x=temp_x_coordinates[i],
                              y=temp_y_coordinates[i],
                              shape='dot',physics=False,size=5
                              )
    data_lineage.add_edges(temp_nodes_edges)
    data_lineage.repulsion(node_distance=70,spring_length=50)
    data_lineage.show("Data_Lineage.html")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()



