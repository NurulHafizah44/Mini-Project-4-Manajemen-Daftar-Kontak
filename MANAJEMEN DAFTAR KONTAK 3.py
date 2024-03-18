import math

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class ContactManager:
    def __init__(self):
        self.head = None

    def create_contact(self, name, phone_number, email):
        new_contact = Node({'name': name, 'phone_number': phone_number, 'email': email})
        if not self.head:
            self.head = new_contact
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_contact
        print("Kontak berhasil ditambahkan.")

    def read_contacts(self):
        current = self.head
        if not current:
            print("Daftar kontak kosong.")
        else:
            print("Daftar Kontak:")
            while current:
                contact = current.data
                print(f"Nama: {contact['name']}, No. Telepon: {contact['phone_number']}, Email: {contact['email']}")
                current = current.next

    def update_contact(self, index, name, phone_number, email):
        current = self.head
        position = 0
        while current and position != index:
            current = current.next
            position += 1
        if not current:
            print("Indeks kontak tidak valid.")
        else:
            current.data = {'name': name, 'phone_number': phone_number, 'email': email}
            print("Kontak berhasil diperbarui.")

    def delete_contact(self, index):
        current = self.head
        if index == 0:
            self.head = current.next
            del current
            print("Kontak berhasil dihapus.")
            return
        position = 0
        while current and position != index - 1:
            current = current.next
            position += 1
        if not current or not current.next:
            print("Indeks kontak tidak valid.")
            return
        deleted_node = current.next
        current.next = deleted_node.next
        del deleted_node
        print("Kontak berhasil dihapus.")
    
    def merge_sort(self, head, key1, key2=None, ascending=True):
        if head is None or head.next is None:
            return head
        
        middle = self.get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        left = self.merge_sort(head, key1, key2, ascending)
        right = self.merge_sort(next_to_middle, key1, key2, ascending)

        sorted_list = self.merge(left, right, key1, key2, ascending)
        return sorted_list

    def merge(self, left, right, key1, key2, ascending):
        if left is None:
            return right
        if right is None:
            return left

        if ascending:
            if left.data[key1] < right.data[key1] or (key2 and left.data[key1] == right.data[key1] and left.data.get(key2, "") < right.data.get(key2, "")):
                result = left
                result.next = self.merge(left.next, right, key1, key2, ascending)
            else:
                result = right
                result.next = self.merge(left, right.next, key1, key2, ascending)
        else:
            if left.data[key1] > right.data[key1] or (key2 and left.data[key1] == right.data[key1] and left.data.get(key2, "") > right.data.get(key2, "")):
                result = left
                result.next = self.merge(left.next, right, key1, key2, ascending)
            else:
                result = right
                result.next = self.merge(left, right.next, key1, key2, ascending)
        
        return result

    def get_middle(self, head):
        if head is None:
            return head
        
        slow = head
        fast = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        return slow

    def sort_contacts(self, key1, key2=None, ascending=True):
        self.head = self.merge_sort(self.head, key1, key2, ascending)

    def jump_search(self, key, key1, key2=None):
        if not self.head:
            print("Daftar kontak kosong.")
            return None

        n = self.length()
        jump = int(math.sqrt(n))
        prev, current = None, self.head

        while current and current.data[key1] < key:
            prev = current
            for _ in range(jump):
                if current.next:
                    current = current.next
                else:
                    break

        while current and current.data[key1] < key:
            current = current.next

        if current and current.data[key1] == key and (not key2 or current.data.get(key2) == key2):
            return current.data
        else:
            print("Kontak tidak ditemukan.")
            return None

    def length(self):
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next
        return length

def main():
    contact_manager = ContactManager()

    while True:
        print("\nPilihan Menu:")
        print("1. Tambah Kontak")
        print("2. Lihat Daftar Kontak")
        print("3. Perbarui Kontak")
        print("4. Hapus Kontak")
        print("5. Urutkan Kontak")
        print("6. Cari Kontak")
        print("7. Keluar")

        choice = input("Masukkan pilihan (1/2/3/4/5/6/7): ")

        if choice == '1':
            name = input("Masukkan nama kontak: ")
            phone_number = input("Masukkan nomor telepon kontak: ")
            email = input("Masukkan email kontak: ")
            contact_manager.create_contact(name, phone_number, email)
        elif choice == '2':
            contact_manager.read_contacts()
        elif choice == '3':
            index = int(input("Masukkan indeks kontak yang akan diperbarui: "))
            name = input("Masukkan nama baru: ")
            phone_number = input("Masukkan nomor telepon baru: ")
            email = input("Masukkan email baru: ")
            contact_manager.update_contact(index, name, phone_number, email)
        elif choice == '4':
            index = int(input("Masukkan indeks kontak yang akan dihapus: "))
            contact_manager.delete_contact(index)
        elif choice == '5':
            key1 = input("Masukkan atribut pertama untuk mengurutkan (misal: name, phone_number, email): ")
            key2 = input("Masukkan atribut kedua untuk mengurutkan (opsional): ")
            while True:
                order = input("Masukkan urutan (asc/desc): ")
                if order.lower() == 'asc' or order.lower() == 'desc':
                    ascending = order.lower() == 'asc'
                    break
                else:
                    print("Urutan tidak valid. Silakan masukkan 'asc' atau 'desc' tanpa spasi tambahan.")
            contact_manager.sort_contacts(key1, key2, ascending)
            print("Kontak berhasil diurutkan.")
        elif choice == '6':
            key1 = input("Masukkan atribut untuk melakukan pencarian (misal: name, phone_number, email): ")
            key2 = input("Masukkan nilai atribut untuk dicari: ")
            result = contact_manager.jump_search(key2, key1)
            if result:
                print("Kontak ditemukan:")
                print(f"Nama: {result['name']}, No. Telepon: {result['phone_number']}, Email: {result['email']}")
        elif choice == '7':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()