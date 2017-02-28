require 'csv'


matches = []
products = []


CSV.foreach("../data/products.csv") do |row|
  products << row[0]
end

CSV.foreach("../data/matches.csv") do |row|
  matches << [row[0], row[1]] if products.include?(row[0]) && products.include?(row[1])
end


matches.uniq!




# CSV.open("workshop.csv", "wb") do |csv|
# 	csv << ["id", "name", attribute_names].flatten
# 	product_id.each.with_index do |id, i|
# 		csv << [id, product_names[i], attributes[i]].flatten
# 	end
# end