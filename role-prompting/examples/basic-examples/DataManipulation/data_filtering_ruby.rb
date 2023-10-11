# Role-prompt: Write a Ruby script that performs data filtering on an array of hashes. The script should be efficient, readable, and handle potential data inconsistencies.

# Sample data: An array of hashes representing people
PEOPLE = [
  { name: "John", age: 30, city: "New York" },
  { name: "Jane", age: 25, city: "San Francisco" },
  { name: "Doe", age: 22, city: "San Francisco" },
  { name: "Smith", age: 20, city: "Boston" },
  # Possible data inconsistency
  { name: "Laura", age: "unknown", city: "Los Angeles" }
]

def filter_people_by_city(people, city)
  """
  Filter the people by the specified city.

  Parameters:
  people (Array): The array of people (each person represented by a hash).
  city (String): The city to filter people by.

  Returns:
  Array: A new array containing people who are from the specified city.
  """

  # Filtering people based on the provided city while handling potential data inconsistencies.
  people.select do |person|
    person[:city] == city && person[:age].is_a?(Integer)
  end
end

def main
  city_to_filter = "San Francisco"
  people_in_sf = filter_people_by_city(PEOPLE, city_to_filter)

  if people_in_sf.any?
    puts "People from #{city_to_filter}:"
    people_in_sf.each { |person| puts "Name: #{person[:name]}, Age: #{person[:age]}" }
  else
    puts "No people from #{city_to_filter} found in the data."
  end
end

# Calling the main function to execute the script
main()
