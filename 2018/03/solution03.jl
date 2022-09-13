data = readlines("input.txt")

function make_nice(s::String)::Vector{String}
    s = replace(s, " @ "=>" ")
    s = replace(s, ","=>" ")
    s = replace(s, "x"=>" ")
    s = replace(s, ": "=>" ")    
    s = replace(s, "#"=>"")
    return split(s, " ")
end

function part1(data::Vector{String})
    board = Dict{Tuple{Int64, Int64}, String}()
    expectation = Dict{String, Int64}()
    for each in data
        box_index, offset_x, offset_y, width_x, width_y = make_nice(each)
        expectation[box_index] = parse(Int64, width_x) * parse(Int64, width_y)
        for x in 1:parse(Int64, width_x)
            for y in 1:parse(Int64, width_y)
                idx = (parse(Int64, offset_x) + x, parse(Int64, offset_y) + y)
                if idx ∈ keys(board)
                    board[idx] = "X"
                else
                    board[idx] = box_index
                end
            end
        end
    end
    p1 = count(==("X"), values(board))
    p2 = "bad"
    for each in keys(expectation)
        if count(==(each), values(board)) == expectation[each]
            p2 = each
        end
    end
    return p1, p2
end

p1, p2 = part1(data)

print("part 1: " * string(p1) * "\n")
print("part 2: " * string(p2))