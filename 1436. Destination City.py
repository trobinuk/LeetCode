class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        lookup = {}
        for path in paths:
            lookup[path[0]] = path[1]
        city = paths[0][0] #B
        while True:
            #if not lookup[city]:
            if city not in lookup:
                return city
            city = lookup[city]