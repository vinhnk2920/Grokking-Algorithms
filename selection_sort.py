import math


def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


if __name__ == '__main__':
    my_list = [5, 3, 6, 2, 10]
    print(selectionSort(my_list))

# TODO: Exercise 2.1:
#  Suppose you’re building an app to keep track of your finances.
#  Every day, you write down everything you spent money on.
#  At the end of the month, you review your expenses and sum up how much you spent.
#  So, you have lots of inserts and a few reads. Should you use an array or a list?

# Read all => Linked list

# TODO: Exercise 2.2:
#  Suppose you’re building an app for restaurants to take customer orders.
#  Your app needs to store a list of orders. Servers keep adding orders to this list,
#  and chefs take orders off the list and make them.
#  It’s an order queue: servers add orders to the back of the queue, and
#  the chef takes the first order off the queue and cooks it.
#  Would you use an array or a linked list to implement this queue?

# Linked list. Lots of inserts are happening (servers adding orders), which linked lists excel at.
# You don’t need search or random access (what arrays excel at), because the chefs always
# take the first order off the queue.

# TODO: Exercise 2.3:
#  Let’s run a thought experiment. Suppose Facebook keeps a list of usernames.
#  When someone tries to log in to Facebook, a search is done for their username.
#  If their name is in the list of usernames, they can log in.
#  People log in to Facebook pretty often, so there are a lot of searches through this list of usernames.
#  Suppose Facebook uses binary search to search the list.
#  Binary search needs random access—you need to be able to get to the middle of the list of usernames instantly.
#  Knowing this, would you implement the list as an array or a linked list?

# You have to select to the middle of list => array

# TODO: Exercise 2.4:
#  People sign up for Facebook pretty often, too.
#  Suppose you decided to use an array to store the list of users. What are the downsides of an array for inserts?
#  In particular, suppose you’re using binary search to search for logins.
#  What happens when you add new users to an array?

# When you lack of place in memory => you have to move user list to another place => O(n)
# Inserting into arrays is slow.
# Also, if you’re using binary search to search for usernames, the array needs to be sorted.
# Suppose someone named Adit B signs up for Facebook.
# Their name will be inserted at the end of the array.
# So you need to sort the array every time a name is inserted!

# TODO: Exercise 2.5:
#  In reality, Facebook uses neither an array nor a linked list to store user information.
#  Let’s consider a hybrid data structure: an array of linked lists.
#  You have an array with 26 slots. Each slot points to a linked list.
#  For example, the first slot in the array points to a linked list containing all the usernames starting with a.
#  The second slot points to a linked list containing all the usernames starting with b, and so on.

# Searching— slower than arrays, faster than linked lists.
# Inserting— faster than arrays, same amount of time as linked lists.
# So it’s slower for searching than an array, but faster or the same as linked lists for everything.
