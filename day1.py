class ElectronicItem:
    def __init__(self, id, name, purchase_date, status='Active'):
        self.id = id
        self.name = name
        self.purchase_date = purchase_date
        self.status = status

    def mark_for_recycling(self):
        self.status = 'Recycling'

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Purchase Date: {self.purchase_date}, Status: {self.status}"


class EWasteMonitoringSystem:
    def __init__(self):
        self.items = {}

    def add_item(self, id, name, purchase_date):
        if id in self.items:
            print(f"Item with ID {id} already exists.")
        else:
            self.items[id] = ElectronicItem(id, name, purchase_date)
            print(f"Item {name} added successfully.")

    def update_item_status(self, id, status):
        if id in self.items:
            if status == 'Recycling':
                self.items[id].mark_for_recycling()
                print(f"Item ID {id} marked for recycling.")
            else:
                print("Invalid status.")
        else:
            print(f"Item with ID {id} not found.")

    def get_item_details(self, id):
        if id in self.items:
            print(self.items[id])
        else:
            print(f"Item with ID {id} not found.")

    def print_all_items(self):
        if self.items:
            for item in self.items.values():
                print(item)
        else:
            print("No items in the system.")

# Example usage
if __name__ == "__main__":
    system = EWasteMonitoringSystem()

    # Adding items
    system.add_item(1, 'Old Laptop', '2021-01-15')
    system.add_item(2, 'Broken Printer', '2020-11-10')

    # Print details of all items
    system.print_all_items()

    # Update status of an item
    system.update_item_status(1, 'Recycling')

    # Print details of a specific item
    system.get_item_details(1)
