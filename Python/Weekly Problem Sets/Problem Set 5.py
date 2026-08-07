import requests


# Problem 1
def recursive_squares(n):
    if type(n) != int:
        return []
    if n < 1:
        return []
    if n == 1:
        return [1]
    else:
        return recursive_squares(n - 1) + [n**2]


def palindrome_checker(word):
    cleaned = word.lower()
    if len(cleaned) < 2:
        return True
    elif cleaned[0] != cleaned[-1]:
        return False
    else:
        return palindrome_checker(cleaned[1:-1])


def length(tlist):
    if tlist:
        return length(tlist[:-1]) + 1
    return 0


def flatten(mixed_list):
    if len(mixed_list) < 1:
        return []
    elif type(mixed_list[0]) == int:
        return [mixed_list[0]] + flatten(mixed_list[1:])
    else:
        return flatten(mixed_list[0]) + flatten(mixed_list[1:])


# Problem 2


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def count_ways(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return count_ways(n - 2) + count_ways(n - 1)


def grid_paths(m, n):
    if m == 1 or n == 1:
        return 1
    else:
        return grid_paths(m, n - 1) + grid_paths(m - 1, n)


def permutation(perm_list):
    if not perm_list:
        return []
    else:
        holder = []
        for i in range(len(perm_list)):
            hold = perm_list[i]
            clone = perm_list[:]
            del clone[i]
            holder.append([hold] + permutation(clone))
        return holder


# Problem 3
base = "https://jsonplaceholder.typicode.com"
chal_base = "https://reqres.in/api/users"


def get_user(user_id: int) -> dict:
    bridge = f"/users/{user_id}"
    holder = requests.get(base + bridge)
    if holder.status_code != 200:
        print(holder.status_code)
        return {}
    else:
        return holder.json()


def create_user(name, job):
    bridge = "/users"
    create_holder = requests.post(base + bridge, {"name": name, "job": job})
    if create_holder.status_code != 201:
        print(create_holder.status_code)
        return {}
    else:
        return create_holder.json()


def update_user(user_id, name, job):
    bridge = f"/users/{user_id}"
    submit_dict = {"name": name, "job": job}
    res_dict = requests.put(base + bridge, json=submit_dict)
    if res_dict.status_code != 200:
        print(res_dict.status_code)
        return {}
    else:
        return res_dict.json()


def delete_user(user_id):
    bridge = f"/users/{user_id}"
    del_dict = requests.delete(base + bridge)
    return del_dict.status_code == 200


def get_all_users_page(page):
    bridge = f"?page={page}"
    header = {"x-api-key": "free_user_3Hb3S2tmGt30vw7rrZkQcl8go3q"}
    chal_page = requests.get(chal_base + bridge, headers=header)
    if chal_page.status_code != 200:
        return []
    else:
        return chal_page.json()["data"]


def partial_update_user(user_id, updates):
    bridge = f"/{user_id}"
    header = {"x-api-key": "free_user_3Hb3S2tmGt30vw7rrZkQcl8go3q"}
    chal_update = requests.patch(chal_base + bridge, headers=header, json=updates)
    if chal_update.status_code != 200:
        return {}
    else:
        return chal_update.json()


if __name__ == "__main__":

    def prob1():
        print(recursive_squares(5))
        print(recursive_squares([]))
        print(palindrome_checker("aab"))
        print(length([5, 6, 7, 8]))
        print(flatten([1, [2, 3], [4], 5]))

    def prob2():
        print(fibonacci(7))
        print(count_ways(4))
        print(grid_paths(3, 3))
        print(permutation([1, 2, 3]))

    def prob3():
        print(get_user(4))
        example_user = {"name": "pat", "job": "army"}
        print(create_user("pat", "army"))
        print(update_user(3, "pat", "job"))
        print(delete_user(3))
        print(get_all_users_page(2))
        print(partial_update_user(2, {"job": "Senior Developer"}))

    # prob1()
    # prob2()
    prob3()
