if choice == '1':
    value = input("Enter value to enqueue: ")
    queue.enqueue(value)
elif choice == '2':
    queue.dequeue()
elif choice == '3':
    queue.display()
elif choice == '4':
    print("Exiting program. Goodbye!")
    break
else:
     print("Invalid choice. Please try again.")



