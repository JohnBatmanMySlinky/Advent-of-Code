function READ()
    data = readlines("input.txt")
    seeds = Int64[parse(Int, String(i)) for i in split(split(popfirst!(data), ": ")[2], " ")]
    _ = popfirst!(data)
    structure = Array{Array{Int64}}[]
    tmp = Array{Int64}[]
    for maps in data
        if !(findfirst(":", maps) isa Nothing)
            continue
        elseif maps == ""
            push!(structure, tmp)
            tmp = []
        else
            push!(tmp, Int64[parse(Int, String(i)) for i in split(maps, " ")])
        end
    end
    push!(structure, tmp)
    return seeds, structure
end


function p2()
    seeds, maps = READ()
    seedranges = UnitRange[x:(x+y-1) for (x,y) in zip(seeds[begin:2:end], seeds[2:2:end])]

    upper_bound = 100_000_000

    winner = 999_999_999_999
    for seed in reverse(1:(upper_bound-1))
        if seed % 1_000_000 == 0
            print("Seed: $(seed), winner: $(winner)\n")
        end
        curr = seed
        for chunk in reverse(maps)
            found = false
            for (dest, inp, r) in chunk
                if curr-dest+inp in inp:(inp+r-1)
                    curr = curr-dest+inp
                    found = true
                end
                if found == true
                    break
                end
            end
        end
        if any(Bool[curr in seedrange for seedrange in seedranges])
            if seed < winner
                winner = seed
            end
        end
    end
    return winner
end

# my back up plan was re-writing this thing as a giant ass piece wise function...

print("$(p2())")