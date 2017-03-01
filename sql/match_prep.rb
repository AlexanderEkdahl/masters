require 'csv'
require 'set'


matches = {}
products = []

# dict = {}


CSV.foreach("../data/subset_no_empty_columns.csv") do |row|
 products << row[0]
 # id = row[0]
 # row.shift(2)
 # dict[id] = row 
end

CSV.foreach("../data/matches.csv") do |row|
  matches[row[1]] = Set.new if !matches.has_key?(row[1])
  matches[row[1]].add(row[0]) if products.include?(row[0])
end


CSV.open("../data/filtered_matches.csv", "wb") do |csv|
	matches.each do |k, v|
		if v.count > 0
			v.each { |x| csv << [x, k].flatten}
		end
	end
end