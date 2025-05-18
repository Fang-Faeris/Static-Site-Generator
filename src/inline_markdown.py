from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in olld_nodes:
        if node.text_type != text_type.TEXT:
            new_nodes.append(node)
            continue
        split_nodes = []
        sections = node.text.split(delimiter)
        for section in sections:
            if len(section) % 2 == 0:
                raise Exception("Invalid Markdown, formatting needs to be closed.")
            for i in range(0, len(section)):
                if section[i] == "":
                    continue
                if section[i] % 2== 0:
                    split_nodes.append(TextNode(section[i], text_type.TEXT))
                else:
                    split_nodes.append(TextNode(section[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes