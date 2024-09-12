class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_lst = path.split('/')
        stack = []
        i = 0
        while i < len(path_lst):
            if not path_lst[i] or path_lst[i] == '.': # Handles the case for consecutive slashes ( /// )
                path_lst.pop(i)
                continue
            elif path_lst[i] == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(path_lst[i])
            i += 1

        return '/' + '/'.join(stack)