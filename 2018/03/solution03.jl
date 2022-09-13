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
    for each in data
        box_index, offset_x, offset_y, width_x, width_y = make_nice(each)
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
    return count(==("X"), values(board))
end

print(part1(data))