

/*Zadanie: Napisz program w języku C#, który będzie umożliwiał zarządzanie listą zwierząt. Program powinien spełniać następujące wymagania.

Każde zwierzę powinno mieć następujące właściwości: nazwę, datę urodzenia, informację czy jest ssakiem i rodzaj (ptak, ryba, gad, płaz lub ssak).
Program powinien umożliwiać dodawanie nowych zwierząt do listy, podając ich właściwości od użytkownika.
Program powinien umożliwiać wyświetlanie listy zwierząt z ich numerami i nazwami.
Program powinien umożliwiać wyświetlanie szczegółów o wybranym zwierzęciu, takich jak opis, wiek i rodzaj.
Program powinien umożliwiać usuwanie wszystkich lub pojedynczego zwierzęcia z listy.
Program powinien mieć menu główne z opcjami do wyboru przez użytkownika.
Program powinien być napisany zgodnie z konwencją nazewnictwa i formatowania kodu w C#.
Wskazówki:

Użyj klasy Animal do reprezentowania zwierzęcia i zdefiniuj jej właściwości, konstruktory i metody.
Użyj typu wyliczeniowego Kind do reprezentowania rodzaju zwierzęcia i zdefiniuj jego wartości.
Użyj listy generycznej List<Animal> do przechowywania zwierząt i korzystaj z jej metod do dodawania, usuwania i wyświetlania elementów.
Użyj klasy Console i jej metod do komunikacji z użytkownikiem i obsługi wejścia i wyjścia.
Użyj instrukcji switch lub if do obsługi różnych opcji menu i wywoływania odpowiednich metod.
Użyj klasy DateTime i jej metod do przechowywania i obliczania daty urodzenia i wieku zwierzęcia*/



using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace ZarzadzanieZwierzetami
{
    public enum Kind { Ptak, Ryba, Gad, Plaz, Ssak }

    public class Animal
    {
        public string Name { get; set; }
        public DateTime BirthDate { get; set; }
        public bool IsMammal { get; set; }
        public Kind AnimalKind { get; set; }

        public Animal(string name, DateTime birthDate, bool isMammal, Kind animalKind)
        {
            Name = name;
            BirthDate = birthDate;
            IsMammal = isMammal;
            AnimalKind = animalKind;
        }

        public int Age
        {
            get { return DateTime.Now.Year - BirthDate.Year; }
        }

        public override string ToString()
        {
            return $"\nNazwa: {Name}, Wiek: {Age}, Rodzaj: {AnimalKind}, Ssak: {IsMammal}";
        }
    }

    internal class Program
    {
        static List<Animal> animals = new List<Animal>();

        static void Main(string[] args)
        {
            InitializeAnimals();
            bool exit = false;

            while (!exit)
            {
                Console.ForegroundColor = ConsoleColor.DarkGreen;
                Console.WriteLine("\n1. Dodaj zwierzę");
                Console.WriteLine("2. Wyświetl listę zwierząt");
                Console.WriteLine("3. Wyświetl szczegóły zwierzęcia");
                Console.WriteLine("4. Usuń zwierzę");
                Console.WriteLine("5. Wyjście");
                Console.ForegroundColor = ConsoleColor.Cyan;
                Console.Write("\nWybierz opcję: ");
                Console.ResetColor();

                int choice;
                if (!int.TryParse(Console.ReadLine(), out choice))
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("\nNieprawidłowa opcja.");
                    Console.ResetColor();
                    continue;
                }

                switch (choice)
                {
                    case 1:
                        AddAnimal();
                        break;
                    case 2:
                        DisplayAnimals();
                        break;
                    case 3:
                        DisplayAnimalDetails();
                        break;
                    case 4:
                        RemoveAnimal();
                        break;
                    case 5:
                        exit = true;
                        break;
                    default:
                        Console.ForegroundColor = ConsoleColor.Red;
                        Console.WriteLine("\nNieprawidłowa opcja.");
                        Console.ResetColor();
                        break;
                }
            }
        }

        static void InitializeAnimals()
        {
            animals.Add(new Animal("Orzeł", new DateTime(2019, 1, 1), false, Kind.Ptak));
            animals.Add(new Animal("Rekin", new DateTime(2014, 3, 15), false, Kind.Ryba));
            animals.Add(new Animal("Krokodyl", new DateTime(2009, 7, 20), false, Kind.Gad));
            animals.Add(new Animal("Żaba", new DateTime(2021, 5, 10), false, Kind.Plaz));
            animals.Add(new Animal("Kot", new DateTime(2017, 9, 5), true, Kind.Ssak));
            animals.Add(new Animal("Papuga", new DateTime(2022, 12, 3), false, Kind.Ptak));
            animals.Add(new Animal("Węgorz", new DateTime(2020, 8, 25), false, Kind.Ryba));
            animals.Add(new Animal("Wąż", new DateTime(2018, 11, 12), false, Kind.Gad));
            animals.Add(new Animal("Pies", new DateTime(2014, 6, 30), true, Kind.Ssak));
            animals.Add(new Animal("Żółw", new DateTime(2010, 4, 18), false, Kind.Gad));
        }

        static void AddAnimal()
        {
            Console.ForegroundColor = ConsoleColor.Cyan;
            Console.Write("\nPodaj nazwę: ");
            string name = Console.ReadLine();

            Console.Write("\nPodaj datę urodzenia (yyyy-mm-dd): ");
            if (!DateTime.TryParse(Console.ReadLine(), out DateTime birthDate))
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("Nieprawidłowa data.");
                Console.ResetColor();
                return;
            }

            Console.Write("\nCzy jest ssakiem? (tak/nie): ");
            bool isMammal = Console.ReadLine().ToLower() == "tak";

            Console.Write("\nPodaj rodzaj (ptak, ryba, gad, plaz, ssak): ");
            if (!Enum.TryParse(Console.ReadLine(), true, out Kind animalKind))
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("\nNieprawidłowy rodzaj.");
                Console.ResetColor();
                return;
            }

            animals.Add(new Animal(name, birthDate, isMammal, animalKind));
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("\n\nZwierzę dodane.");
            Console.ResetColor();
        }

        static void DisplayAnimals()
        {
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.WriteLine("\nLista zwierząt:");
            for (int i = 0; i < animals.Count; i++)
            {
                Console.WriteLine($"{i + 1}. {animals[i].Name}");
            }
            Console.ResetColor();
        }

        static void DisplayAnimalDetails()
        {
            Console.Write("\nPodaj numer zwierzęcia: ");
            if (!int.TryParse(Console.ReadLine(), out int index))
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("\nNieprawidłowy numer.");
                Console.ResetColor();
                return;
            }

            index -= 1;
            if (index >= 0 && index < animals.Count)
            {
                Console.ForegroundColor = ConsoleColor.Yellow;
                Console.WriteLine("\nSzczegóły zwierzęcia:");
                Console.WriteLine($"Nazwa: {animals[index].Name}");
                Console.WriteLine($"Wiek: {animals[index].Age}");
                Console.WriteLine($"Rodzaj: {animals[index].AnimalKind}");
                Console.WriteLine($"Ssak: {animals[index].IsMammal}");
                Console.ResetColor();
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("\nNie ma takiego zwierzęcia.");
                Console.ResetColor();
            }
        }

        static void RemoveAnimal()
        {
            Console.Write("\nPodaj numer zwierzęcia do usunięcia (0 aby usunąć wszystkie): ");
            if (!int.TryParse(Console.ReadLine(), out int index))
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("\nNieprawidłowy numer.");
                Console.ResetColor();
                return;
            }

            index -= 1;
            if (index == -1)
            {
                animals.Clear();
                Console.ForegroundColor = ConsoleColor.Green;
                Console.WriteLine("\nWszystkie zwierzęta zostały usunięte.");
                Console.ResetColor();
            }
            else if (index >= 0 && index < animals.Count)
            {
                animals.RemoveAt(index);
                Console.ForegroundColor = ConsoleColor.Green;
                Console.WriteLine("\nZwierzę usunięte.");
                Console.ResetColor();
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("\nNie ma takiego zwierzęcia.");
                Console.ResetColor();
            }
        }
    }
}