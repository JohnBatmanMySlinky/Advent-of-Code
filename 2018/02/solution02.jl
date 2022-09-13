data = readlines("input.txt")

function checksum(data::Vector{String})
    two = 0
    three = 0
    for id in data
        two_done = false
        three_done = false
        for letter in Set(id)
            if count(==(letter), id)==2
                if !two_done
                    two += 1
                end
                two_done = true
            elseif count(==(letter), id)==3
                if !three_done
                    three += 1
                end
                three_done = true
            end
        end
    end
    return two * three
end

function find_id(data::Vector{String})
    num_boxes = length(data)
    for x in 1:num_boxes
        for y in (x+1):num_boxes
            compare = sum(
                split(data[x],"") .!= split(data[y], "")
            )
            if compare == 1
                answer = ""
                for z in 1:length(data[x])
                    if split(data[x],"")[z] == split(data[y],"")[z]
                        answer *= split(data[x],"")[z]
                    end
                end
                return answer
            end
        end
    end
end

print("part 1: " * string(checksum(data)) * "\n")
print("part 1: " * string(find_id(data)))