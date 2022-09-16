# find bounding box.
# add a layer around the outside
# any coords that don't have a closest in that extra layer are contained. 

data = readlines("input.txt")

function make_nice(s::String)::Vector{Int64}
    return parse.(Int64, split(s, ", "))
end

function bounding_box(b::Vector{Tuple{Int64,Int64}})::Tuple{Int64, Int64, Int64, Int64}
    min_x, min_y = typemax(Int64), typemax(Int64)
    max_x, max_y = typemin(Int64), typemin(Int64)
    for (x,y) in b
        x < min_x && (min_x = x)
        y < min_y && (min_y = y)
        x > max_x && (max_x = x)
        y > max_y && (max_y = y)
    end
    return min_x, min_y, max_x, max_y
end

function manhattan(x1,y1,x2,y2)
    return abs(x1-x2) + abs(y1-y2)
end

function find_nearest(x::Int64, y::Int64, board::Vector{Tuple{Int64, Int64}})
    winner_coord = (99999, 99999)
    winner_distance = typemax(Int64)
    for (a,b) in board
        d = manhattan(x,y,a,b)
        if d < winner_distance
            winner_distance = d
            winner_coord = (a,b)
        end
    end
    return winner_coord
end

function p1(lines::Vector{String})
    board = Tuple{Int64,Int64}[]
    for (i, line) in enumerate(lines)
        x, y = make_nice(line)
        push!(board, (x,y))
    end

    seen = []
    min_x, min_y, max_x, max_y = bounding_box(board)
    # print("min: " * string(min_x) * ", " * string(min_y) * "\n")
    # print("max: " * string(max_x) * ", " * string(max_y) * "\n")

    # loop through vertical sides
    for x in [min_x-1, max_x+1]
        for y in (min_y-1):(max_y+1)
            nearest = find_nearest(x,y,board)
            !(nearest ∈ seen) && (push!(seen, nearest))
        end
    end
    # loop through vertical sides
    for y in [min_y-1, max_y+1]
        for x in (min_x-1):(max_x+1)
            nearest = find_nearest(x,y,board)
            !(nearest ∈ seen) && (push!(seen, nearest))
        end
    end

    finites = []
    for each in board
        !(each ∈ seen) && (push!(finites, each))
    end

    answer = Dict{Tuple{Int64, Int64}, Int64}()
    for each in finites
        answer[each] = 0
    end
    for x in (min_x-1):(max_x+1)
        for y in (min_y-1):(max_y+1)
            log_d = Int64[]
            log_ab = Tuple{Int64, Int64}[]
            for (i, (a,b)) in enumerate(board)
                push!(log_d, manhattan(x,y,a,b))
                push!(log_ab, (a,b))
            end
            min_d = minimum(log_d)
            if count(==(min_d), log_d) == 1
                ab = log_ab[argmin(log_d)]
                if ab ∈ keys(answer)
                    answer[ab] += 1
                end
            end
        end
    end
    return findmax(answer)
end

function p2(lines::Vector{String}, cap::Int64)
    board = Tuple{Int64,Int64}[]
    for (i, line) in enumerate(lines)
        x, y = make_nice(line)
        push!(board, (x,y))
    end

    seen = []
    min_x, min_y, max_x, max_y = bounding_box(board)

    acceptable = 0
    for x in min_x:max_x
        for y in min_y:max_y
            cumulative = 0
            for (a,b) in board
                cumulative += manhattan(x,y,a,b)
            end
            if cumulative < cap
                acceptable += 1
            end
        end
    end
    return acceptable
end

print("part 1: " * string(p1(data)[1]) * "\n")
print("part 2: " * string(p2(data, 10000)))