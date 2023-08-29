function make_grid(serial::Int64, SIZE::Int64)::Matrix{Float64}
    grid = zeros(Int64, SIZE, SIZE)

    for x in 1:SIZE
        for y in 1:SIZE
            rack_id = x + 10
            grid[x, y] = (((rack_id * y + serial) * rack_id) % 1000) ÷ 100 - 5
        end
    end
    return grid
end

function p1(grid::Matrix{Float64}, SIZE::Int64)
    winner = -100
    winner_coord = (-1, -1)
    offsets = [(x,y) for x in -1:1 for y in -1:1]
    for x in 2:(SIZE-1)
        for y in 2:(SIZE-1)
            tot = 0
            for (xo, yo) in offsets
                tot += grid[x+xo, y+yo]
            end
            if tot > winner
                winner = tot
                winner_coord = (x-1, y-1)
            end
        end
    end
    return winner_coord, winner
end

function p2(grid::Matrix{Float64}, SIZE::Int64)
    winner = -1
    winner_coord = (-1, -1, -1)
    for x in 1:SIZE
        for y in 1:SIZE
            for z in 1:(SIZE - max(x,y))
            # for z in 1:(min(17,SIZE - max(x,y)))
                tot = 0
                for xo in 1:z
                    for yo in 1:z
                        tot += grid[x+xo, y+yo]
                    end
                end
                if tot > winner
                    winner = tot
                    winner_coord = (x,y,z)
                end
            end
        end
    end
    return winner_coord, winner
end


g = make_grid(5153, 300)
(x,y), winner = p1(g, 300)
print("Part1: $(x),$(y) with score $(winner)\n")

g = make_grid(5153, 300)
(x,y,z), winner = p2(g, 300)
print("Part2: $(x+1),$(y+1),$(z) with score $(winner)")


