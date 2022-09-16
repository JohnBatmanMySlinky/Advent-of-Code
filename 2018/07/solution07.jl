data = readlines("input.txt")

function make_nice(s::Vector{String})::Vector{Tuple{String,String}}
    new = Tuple{String,String}[]
    for each in data
        push!(new,(
            string(replace(replace(match(r"Step ((\w+\s)|(\w\s))", each).match, "Step " => ""), " " => "")),
            String(replace(replace(match(r"step ((\w+\s)|(\w\s))", each).match, "step " => ""), " " => ""))
        ))
    end
    return new
end

function find_root(tree::Vector{Tuple{String, String}})
    vals = [s for (f,s) in tree]
    winners = Set{String}([])
    for (k,v) in tree
        if !(k ∈ vals)
            push!(winners, k)
        end
    end
    return sort!(collect(winners))
end

function traverse(tree::Vector{Tuple{String, String}})
    q = find_root(tree)
    answer = ""
    while length(q) > 0
        current = popfirst!(q)
        answer *= current
        for (k,v) in tree
            if k == current
                check = true
                # check dependencies
                for (k2,v2) in tree
                    if !(k2 ∈ split(answer, "")) && v2 == v
                        check = false
                    end
                end
                if check == true
                    push!(q, v)
                end
            end
        end
        sort!(q)
    end
    return answer
end

print(traverse(make_nice(data)), "\n")