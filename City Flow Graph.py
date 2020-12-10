# Challenge
# Have the function CityTraffic(strArr) read strArr which will be a representation
# of an undirected graph
# in a form similar to an adjacency list. Each element in the input will contain
# an integer which will
# represent the population for that city, and then that will be followed by
# a comma separated list of
# its neighboring cities and their populations (these will be separated by a colon).
# For example: strArr may be
# ["1:[5]", "4:[5]", "3:[5]", "5:[1,4,3,2]", "2:[5,15,7]", "7:[2,8]", "8:[7,38]", "15:[2]", "38:[8]"].
# This graph then looks like the following picture:

# Each node represents the population of that city and each edge represents a road to that city.
# Your goal is to determine the maximum traffic that would occur via a single road if everyone decided to go to that city.
# For example: if every single person in all the cities decided to go to city 7, then via the upper road the
# number of people coming in would be (8 + 38) = 46. If all the cities beneath city 7 decided to go to it via
# the lower road, the number of people coming in would be (2 + 15 + 1 + 3 + 4 + 5) = 30.
# So the maximum traffic coming into the city 7 would be 46 because the maximum value of (30, 46) = 46.
# Your program should determine the maximum traffic for every single city and return the answers in a
# comma separated string in the format: city:max_traffic,city:max_traffic,...
# The cities should be outputted in sorted order by the city number.
# For the above example, the output would therefore be:
# 1:82,2:53,3:80,4:79,5:70,7:46,8:38,15:68,38:45.
# The cities will all be unique positive integers and there will not be any cycles in the graph.
# There will always be at least 2 cities in the graph.
# Hard challenges are worth 15 points and you are not timed for them.

# Sample Test Cases:

in1 = "1:[5]", "2:[5]", "3:[5]", "4:[5]", "5:[1,2,3,4]"
out1 = "1:14,2:13,3:12,4:11,5:4"

in2 = "1:[5]", "2:[5,18]", "3:[5,12]", "4:[5]", "5:[1,2,3,4]", "18:[2]", "12:[3]"
out2 = "1:44,2:25,3:30,4:41,5:20,12:33,18:27"

in3 = "1:[5]", "4:[5]", "3:[5]", "5:[1,4,3,2]", "2:[5,15,7]", "7:[2,8]", "8:[7,38]", "15:[2]", "38:[8]"
out3 = "1:82,2:53,3:80,4:79,5:70,7:46,8:38,15:68,38:45"

in4 = "4:[100]", "100:[4,67]", "67:[100,12]", "12:[67]"
out4 = "4:179,12:171,67:104,100:79"

in5 = "4:[100]", "100:[4,67]", "67:[100,12,89]", "12:[67]", "89:[67]"
out5 = "4:268,12:260,67:104,89:183,100:168"

in6 = "12:[4]", "82:[4]", "4:[12,82,90]", "90:[4,105]", "105:[90]"
out6 = "4:195,12:281,82:211,90:105,105:188"

in7 = "1:[5]", "4:[5]", "3:[5]", "5:[1,4,3,2]", "2:[5,15,7]", "7:[2,8]", "8:[7,38]", "15:[2]", "38:[8,104]", "104:[38]"
out7 = "1:186,2:157,3:184,4:183,5:174,7:150,8:142,15:172,38:104,104:83"

in8 = "56:[2]", "2:[56,12]", "3:[12]", "12:[2,3]"
out8 = "2:56,3:70,12:58,56:17"



ins = [in1, in2, in3, in4, in5, in6, in7, in8]
outs = [out1, out2, out3, out4, out5, out6, out7, out8]


def test_func():    # Run pytest file.py to test using this func.
    for i, j in zip(ins, outs):
        assert max_traffic(i) == j


"""
Solution :

Construct the output dictionary.
For Each node :
    Follow node and get its neighbours
    Create n separate 'Groups', one for each neighbour
    for each group :
        for each node follow nodes & add neighbours to the group (if not already there (avoid repetition) & if it is not the main group caller).
        .....do this till you have nothing new to add (len_before == len_after)
        now sum the contents of each group
    compare them (if there is more than one!) and return the largest group value
    append this {node:max_group_value} to the output dictionary.
Return the output dictionary.
"""

# import ast
# ast.literal_eval()
# Parse a string literal as a legit python datatype https://stackoverflow.com/a/1894296/9053193

def max_traffic(city_graph):

    city_graph = eval(
        str(city_graph).replace("'", "").replace("(", "{").replace(")", "}"))

    out = {}
    groups = {}

    for i in city_graph:
        out[i] = []
        groups[i] = [[x] for x in city_graph[i]]

        for group in groups[i]:
            for node in group:
                neibs = city_graph[node]
                [group.append(n) for n in neibs if n not in group and n not in [i]]
            out[i] += [sum(group)]
        out[i] = max(out[i])

    return str({i: out[i] for i in sorted(out)}).strip("{}").replace(" ", "")
