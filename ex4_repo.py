"""
Contains 2 classes for Version control of single information pieces, like numbers:
- "Commit" with information about a single commit
- "Repo" with information about commits of numbers
"""


class Commit:

    def __init__(self, message, nums_added_changed=None, prev_commit=None):
        """
        Initiate a single Commit with information about commit message, what numbers were changed
            and snapshot of all numbers.
            Each number versioned has a "name" and a "value".
            Values can be updated for existing number, but a number can not be deleted.

        :param message: commit message that explains the commit
        :param nums_added_changed: dictionary of {number_name: number_value}
            of numbers that were added or changed in the current commit.
            If not given (None) - assumed that no numbers were changed
                (valid only for initial commit of creation of repo)
        :param prev_commit: Instance of Commit class of the previous commit.
            If not given (None) - assumed that this is the first commit of the repository
        """
        if type(message) != str:
            raise TypeError(f"Error: commit message expects a string but received {type(message)}!")
        else:
            self.message = message

        if prev_commit is None:
            self.nums_all = {}
        elif not isinstance(prev_commit, Commit):
            raise TypeError(f"Error: commit nums_added_changed expects a Commit object but received {type(prev_commit)}!")
        else:
            self.nums_all = prev_commit.nums_all

        if nums_added_changed is None:
            self.nums_added_changed = {}
        elif type(nums_added_changed) != dict:
            raise TypeError(f"Error: commit nums_added_changed expects a dictionary but received {type(nums_added_changed)}!")
        elif not all([True if type(name) == str and (type(value) is int or type(value) is float) else False for name, value in nums_added_changed.items()]):
            raise TypeError("Error: commit nums_added_changed values are invalid! expecting a dictionary from the form of: {string: int or float}.")
        else:
            self.nums_added_changed = nums_added_changed
            self.nums_all.update(self.nums_added_changed)

    def __getitem__(self, item):
        return self.nums_all[item]

    def __str__(self):
        """
        Returns string representation of a Commit
        Example of a string: 'Commit message: "msg3", 2 numbers added/changed, 3 total numbers'

        :return: String representation of a Commit (see example above)
        """
        return f'Commit message: "{self.message}", {len(self.nums_added_changed)} numbers added/changed, {len(self.nums_all)} total numbers'


class Repo:

    def __init__(self, repo_name, initial_commit_msg):
        """
        Initialize an empty repository with an "empty" commit (no numbers)
        :param repo_name: name of repository to initialize
        :param initial_commit_msg: commit message of the initial commit
        """
        if type(repo_name) != str or type(initial_commit_msg) != str:
            raise TypeError(f'class Repo expects repo_name: str, initial_commit_msg: str ,but received '
                            f'repo_name: {type(repo_name)}, initial_commit_msg: {type(initial_commit_msg)}!')
        self.repo_name = repo_name
        self.initial_commit_msg = initial_commit_msg
        self.staged = {}
        self.commits = []
        self.commit(self.initial_commit_msg)

    def stage(self, num_name, num_value):
        """
        Stage a number with the given value
        :param num_name: name of number to stage
        :param num_value: value of number to stage
        """
        if type(num_name) != str or (type(num_value) != int and type(num_value) != float):
            raise TypeError(f'Error: stage function expects num_name: str, num_value: int or float, '
                            f'but received num_name: {type(num_name)}, num_value: {type(num_value)}!')
        else:
            self.staged.update({num_name: num_value})

    def commit(self, message):
        """
        Commit staged numbers
        :param message: commit message of the commit
        """
        if type(message) != str:
            raise TypeError(f'class Repo expects message: str, but received message: {type(message)}!')
        elif not self.staged and not self.commits:
            self.commits.append(Commit(message=message))
        elif not self.staged:
            print("nothing to commit.\nstage number first and then commit.")
        else:
            self.commits.append(Commit(message=message, nums_added_changed=self.staged, prev_commit=self.commits[-1]))
            self.staged = {}

    def __getitem__(self, item):
        """
        enable use [] in order to get back specific value.
        in case item is a string the function return stagged[item] value. in case item is an integer the function will
        return commits[item]
        :param item:
        """
        if type(item) == str:
            return self.staged[item]
        elif type(item) == int:
            return self.commits[item]
        else:
            raise TypeError(f'Error: __getitem__ expects either string or integer but received {type(item)}!')

    def __str__(self):
        return f'Repo "My Repo", {len(self.commits)} commits, {len(self.staged)} numbers staged'
