from KripkeStructureFramework.KripkeStructure import KripkeStructure
from KripkeStructureFramework.Node import Node
import random
import jsonpickle


class SystemFactory:
    """
    This class handles the generation, import and export of systems that are implemented as Kripke Structures.
    """

    @staticmethod
    def create_system(density=10, size=10, attribute="q", initials_density=10, attribute_probability=30):
        """
        :param density: Structure's density: between 0 and 100 percents.
        :type density: int, float
        :param size: number of nodes in the structure
        :type size: int
        :param attribute: attributes that may be added to each node
        :type attribute: list of strings
        :param initials_density: amount of initial states, 10 means 10% of nodes are initials, 0 means 1 initial node
        :type initials_density: int
        :param attribute_probability: the probability of an attribute to appear on a node, between 0 and 100.
        :type attribute_probability: int
        :return: Kripke structure with the desired parameters
        :rtype:  Kripke Structure
        """
        # region initialization
        nodes = []
        relations = []
        current_relations_count = 0
        all_system_indexes = set(range(0, size))
        num_of_initials = size * (initials_density / 100)
        if num_of_initials < 1:
            num_of_initials = 1
        if num_of_initials > size:
            num_of_initials = size
        # endregion

        # region Generate nodes
        for i in range(0, size):
            attributes = [attribute, ""]
            # node_attribute will store a list of 1 attribute according to the given probability:
            node_attribute = random.choices(attributes, weights=[attribute_probability, 100 - attribute_probability], k=1)
            # create a new node according the parameters:
            nodes.append(Node(i, node_attribute[0], num_of_initials > 0))
            num_of_initials = num_of_initials - 1
        # endregion

        # region Generate relations
        # region 100percent density case
        if density == 100:
            for node in nodes:
                node.relations = all_system_indexes  # each nodes is connected to the entire nodes in the system
            return KripkeStructure(nodes)
        # endregion

        # region general case
        # create relations:
        # generate minimum required relations:
        node_ids = list(range(0, size))
        random.shuffle(node_ids)
        # get random initial node:
        for node_id in node_ids:
            if nodes[node_id].isInitial:
                first_node = node_id
                node_ids.pop(node_ids.index(first_node))
                break
        # create the minimum relations:
        current_node_id = first_node
        for i in node_ids:
            nodes[current_node_id].add_relation(i)
            current_relations_count = +1
            current_node_id = i
        # now connect last node to another node:
        rand_node_id = random.randint(0, size - 1)
        nodes[current_node_id].add_relation(rand_node_id)

        # add the rest of the relations:

        # minimum relations amount at 0%: size
        # maximum relations amount at 100%: size^2
        # we need: ((density/100) * (size^2 - size))
        remaining_relations = int((density / 100) * ((size ** 2) - size))
        while remaining_relations > 0:
            rand_node_id = random.randint(0, size - 1)
            chosen_node = nodes[rand_node_id]
            if len(chosen_node.relations) >= size:
                continue
            # create complement relation list:
            complement_set = all_system_indexes - chosen_node.relations
            chosen_node.add_relation(random.sample(complement_set, 1)[0])
            remaining_relations -= 1
        # endregion
        # endregion

        return KripkeStructure(nodes)

    @staticmethod
    def export_system(path, file_name, system):
        '''
        This methods exports a kripke structure to a .json file on the file system
        :param path: path to the wanted folder
        :type path:
        :param file_name: desired file name
        :type file_name:
        :param system: kripke structure
        :type system:
        :return:
        :rtype:
        '''
        json_object = jsonpickle.encode(system)
        # json.dumps(system)
        # Writing to sample.json
        print(json_object)
        with open(file_name, "w") as outfile:
            outfile.write(json_object)

    @staticmethod
    def import_system(file_path):
        '''
        This methods creates a kripke structure from a .json file
        :param file_path: path to the .json file
        :type file_path:
        :return: Kripke structure
        :rtype:
        '''
        with open(file_path) as f:
            data = f.read()
        ks = jsonpickle.decode(data)
        return ks
