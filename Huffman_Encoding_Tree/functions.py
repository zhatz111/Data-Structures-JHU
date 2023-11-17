"""This file contains two classes: Node and HuffmanEncoding. The Node class represents 
a node in the Huffman tree, which has attributes for frequency, symbol, left child, 
right child, and Huffman code. The HuffmanEncoding class implements the Huffman encoding 
algorithm, which is a lossless data compression technique. The class contains methods 
for building the Huffman tree, encoding and decoding data using the tree, and calculating 
the space reduction achieved by the compression. The encoding and decoding processes are 
performed by traversing the tree and assigning codes to each symbol. The class uses the 
Node class to represent the nodes in the tree.
"""
class Node:
    """
    Represents a node in the Huffman tree.

    A `Node` object represents a node in the Huffman tree. Each node has a frequency,
    a symbol, a left child node, a right child node, and a code (which is used to generate
    the Huffman codes). If the node is a leaf node, its symbol represents a character
    in the input data and its frequency represents the number of times that character
    appears in the input data. If the node is not a leaf node, its symbol is the concatenated 
    child characters and its frequency represents the sum of the frequencies of its children.

    Parameters:
    -----------
    freq : int
        The frequency of the symbol represented by the node (if the node is a leaf node),
        or the sum of the frequencies of its children (if the node is not a leaf node).
    symbol : str
        The symbol represented by the node.
    left : Node or None, optional (default=None)
        The left child node of the current node. If the node is a leaf node, the `left`
        argument should be set to None.
    right : Node or None, optional (default=None)
        The right child node of the current node. If the node is a leaf node, the `right`
        argument should be set to None.

    Attributes:
    -----------
    freq : int
        The frequency of the symbol represented by the node (if the node is a leaf node),
        or the sum of the frequencies of its children (if the node is not a leaf node).
    symbol : str
        The symbol represented by the node.
    left : Node or None
        The left child node of the current node. If the node is a leaf node, `left` is None.
    right : Node or None
        The right child node of the current node. If the node is a leaf node, `right` is None.
    code : str
        The Huffman code for the symbol represented by the node. This is set during the
        Huffman tree traversal.

    """
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.code = ""

class NodeSorter:
    """A sorting class for sorting a list of Node objects based on two keys.

    Attributes:
        key1 (str): The name of the first key to sort by.
        key2 (str): The name of the second key to sort by.

    Methods:
        sort(nodes): Sorts a list of Node objects based on the two keys.
    
    Example usage:
        nodes = [Node(3, 1), Node(1, 2), Node(2, 2)]
        sorter = NodeSorter('key1', 'key2')
        sorter.sort(nodes)
    """
    def __init__(self, key1_func, key2_func):
        self.key1_func = key1_func
        self.key2_func = key2_func

    def sort(self, nodes):
        """Sorts a list of Node objects based on the two keys.

        Args:
            nodes (list): A list of Node objects to sort.

        Returns:
            None.

        Example usage:
            nodes = [Node(3, 1), Node(1, 2), Node(2, 2)]
            sorter = NodeSorter('key1', 'key2')
            sorter.sort(nodes)
        """
        for i, _ in enumerate(nodes):
            min_idx = i
            for j in range(i+1, len(nodes)):
                if self.key1_func(nodes[j]) < self.key1_func(nodes[min_idx]):
                    min_idx = j
                elif self.key1_func(nodes[j]) == self.key1_func(nodes[min_idx]) and \
                self.key2_func(nodes[j]) < self.key2_func(nodes[min_idx]):
                    min_idx = j
            nodes[i], nodes[min_idx] = nodes[min_idx], nodes[i]

class HuffmanEncoding:
    """
    A class for Huffman Encoding, a lossless data compression algorithm.

    Attributes:
        file_path (str): Path to the text file to be compressed/decompressed.
        freq_table (dict): Dictionary mapping each character in the text file to its frequency.
        codes (dict): Dictionary mapping each character in the text file to its Huffman code.
        total_freq (dict): Dictionary mapping each character in the text file to its total 
        frequency in the Huffman tree.
    
    Methods:
        file_to_dict(): Reads the text file and converts it to a dictionary with each line having
        a key and value associated.
        build_huffman_tree(): Builds a Huffman tree using the frequency table of the text file.
        preorder_traversal(node, prefix=''): Recursively prints the preorder traversal of the 
        Huffman tree.
        huffman_encoding(data, compression_type="Encode"): Encodes or decodes the given data based 
        on the compression type.
    """

    def __init__(self, file_path):
        self.file_path = file_path
        self.freq_table = {}
        self.total_freq = {}
        self.codes = {}

    def file_to_dict(self):
        """
        Reads in a text file and converts it to a frequency table.

        This method reads in a text file and creates a dictionary
        representing the frequency of each character in the file.
        The dictionary keys are the unique characters in the file,
        and the values are the number of times each character appears.
        The resulting dictionary is stored as the `freq_table` attribute
        of the HuffmanEncoder instance.

        Parameters:
        -----------
        None

        Returns:
        --------
        None

        Updates the `freq_table` attribute of the HuffmanEncoder instance.
        """
        with open(self.file_path, encoding="utf-8") as file:
            for line in file:
                try:
                    key = line.strip().split()[0]
                    value = int(line.strip().split()[2])
                    self.freq_table[key] = value
                except IndexError:
                    print(f"The line [{line}] in the frequency table text",
                          "file is not in the correct format and will be ignored!")
                

    def preorder_traversal(self, node, prefix=''):
        """
        Preorder traversal of a binary tree to generate Huffman codes and total 
        frequency of symbols.

        Args:
        - node: A node in the binary tree.
        - prefix: A string representing the prefix code for the current node.

        Returns:
        - None.

        If the left or right child of the current node is None, the function assigns 
        the prefix code to the symbol and the total frequency of the symbol in the 
        tree. Otherwise, the function recursively traverses the left and right subtrees 
        of the current node and generates prefix codes for the symbols in the subtrees.
        """
        if (node.left is None) or (node.right is None):
            # print(f"{node.symbol}: {prefix}")
            self.codes[node.symbol] = prefix
            self.total_freq[node.symbol] = node.freq
        else:
            self.total_freq[node.symbol] = node.freq
            self.preorder_traversal(node.left, prefix + '0')
            self.preorder_traversal(node.right, prefix + '1')

    def calculate_space_reduction(self, data, encoded_str, file=None):
        """
        Calculates the space reduction achieved by Huffman compression.

        Given the original data `data` and the compressed data `encoded_str`
        obtained using the Huffman coding algorithm, this function calculates
        the space reduction achieved by the compression as a percentage of the
        space needed to store the original data.

        Parameters:
        -----------
        data : bytes
            The original data that needs to be compressed.
        encoded_str : str
            The compressed data obtained using the Huffman coding algorithm.

        Returns:
        --------
        None

        Prints the space needed before and after Huffman compression, as well as
        the percentage reduction in space achieved.

        """
        pre_compression = len(data) * 8
        post_compression = len(encoded_str)
        reduction = ((pre_compression-post_compression)/pre_compression)*100
        print(f"Space needed before Huffman Compression (bits): {pre_compression}", file=file)
        print(f"Space needed after Huffman Compression (bits): {post_compression}", file=file)
        print(f"Space reduction of {reduction:.2f}%\n", file=file)

    def build_huffman_tree(self):
        """
        Builds a Huffman tree from the frequency table generated by the `file_to_dict` method.

        This method creates a list of `Node` objects based on the frequency table
        generated by the `file_to_dict` method. It then constructs a Huffman tree
        by iteratively merging the two nodes with the lowest frequency, until only
        a single root node remains. The code for each node is determined by its position
        in the tree, with left children receiving a `0` code and right children receiving
        a `1` code. The function returns the root node of the resulting Huffman tree.

        Parameters:
        -----------
        None

        Returns:
        --------
        Node
            The root node of the Huffman tree constructed from the frequency table.

        """
        self.file_to_dict()
        symbols = self.freq_table.keys()

        nodes = []

        for symbol in symbols:
            nodes.append(Node(self.freq_table.get(symbol), symbol))

        while len(nodes) > 1:
            sorter = NodeSorter(lambda node: node.freq, lambda node: node.symbol[::-1])
            sorter.sort(nodes)

            if (nodes[0].freq == nodes[1].freq) and (len(nodes[0].symbol) > len(nodes[1].symbol)):
                left = nodes[1]
                right = nodes[0]
            else:
                left = nodes[0]
                right = nodes[1]

            left.code = 0
            right.code = 1

            new_node = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
            nodes.remove(left)
            nodes.remove(right)
            nodes.append(new_node)

        self.preorder_traversal(nodes[0])
        return nodes[0]


    def huffman_encoding(self, data, compression_type="Encode"):
        """
        Encodes or decodes the input data using Huffman coding.

        This method takes in the input data and encodes or decodes it using
        Huffman coding. The type of compression to perform is determined by
        the `compression_type` argument, which can be either "Encode" or "Decode".
        If "Encode", the input data is encoded using the Huffman codes generated
        from the frequency table. If "Decode", the input data is decoded using
        the Huffman tree generated from the frequency table.

        Parameters:
        -----------
        data : str
            The input data to compress or decompress.
        compression_type : str, optional (default="Encode")
            The type of compression to perform. Can be either "Encode" or "Decode".

        Returns:
        --------
        str
            The encoded or decoded data, depending on the `compression_type`.
            If the `compression_type` is not "Encode" or "Decode", returns an error message.
        """
        node = self.build_huffman_tree()

        if compression_type == "Encode":
            encoded_str = ""
            for char in data:
                try:
                    encoded_str += self.codes.get(char.upper())
                except TypeError:
                    pass
            return encoded_str

        if compression_type == "Decode":
            decoded_str = ""
            root_node = node
            for code in str(data):
                if code == "0":
                    root_node = root_node.left
                elif code == "1":
                    root_node = root_node.right
                if (root_node.left is None) and (root_node.right is None):
                    decoded_str += root_node.symbol
                    root_node = node
            return decoded_str

        return "Error: Your compression can not proceed as the compression \
                type you provided is invalid!"
