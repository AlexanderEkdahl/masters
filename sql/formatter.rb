require 'json'
require 'csv'

product_id = []
product_names = []
attributes = []
attribute_names = []

CSV.foreach("../data/subset.csv") do |row|
  product_id << row[0]
  product_names << row[1]
  attributes << JSON.parse(row[2])
end

CSV.foreach("../data/subset_attributes.csv") do |row|
  attribute_names << row[0]
end

(attribute_names.count - 1).downto(0).each do |i|
	found = false

	attributes.each.with_index do |_, j|
		if attributes[j][i] != nil
			found = true
			break
		end
	end

	if !found
		attribute_names.delete_at(i)
		attributes.each do |attribute_values|
			attribute_values.delete_at(i)
		end
	end
end

CSV.open("workshop.csv", "wb") do |csv|
	csv << ["id", "name", attribute_names].flatten
	product_id.each.with_index do |id, i|
		csv << [id, product_names[i], attributes[i]].flatten
	end
end