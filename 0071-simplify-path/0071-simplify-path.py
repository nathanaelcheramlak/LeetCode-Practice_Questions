class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_lst = path.split('/')
        stack = []

        for i in range(len(path_lst)):
            if path_lst[i] and path_lst[i] != '.':
                if path_lst[i] == '..':
                    if stack:
                        stack.pop()
                else:
                    stack.append(path_lst[i])

        return '/' + '/'.join(stack)