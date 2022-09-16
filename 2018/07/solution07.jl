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

function make_timer(offset::Int64)::Dict{String,Int64}
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    d = Dict{String,Int64}()
    for (i, l) in enumerate(split(letters,""))
        d[string(l)] = i + offset
    end
    return d
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

function traverse_timed(tree::Vector{Tuple{String, String}}, N::Int64, offset::Int64=0)
    workers = String[]
    advanced = String[]
    t = make_timer(offset)
    q = find_root(tree)
    answer = ""
    i = 0
    while (length(q) > 0) | (length(workers) > 0)
        i += 1
        for n in 1:N
            if (length(q) > 0) && (length(workers) < N)
                tmp = popfirst!(q)
                push!(workers, tmp)
            end
        end
        to_be_deleted = []
        for (ii, w) in enumerate(workers)
            t[w] -= 1
            if t[w] == 0
                push!(advanced, w)
                push!(to_be_deleted, w)
            end
        end
        workers = [x for x in workers if !(x ∈ to_be_deleted)]

        # print(i, "\n")
        # print("workers ", workers, "\n")
        # print("advanced ", advanced, "\n")
        # print("answer ", answer, "\n")
        # print(q, "\n")
        # print([x for x in t if (x.first in workers) | (x.first in advanced) | (x.first in split(answer, ""))], "\n")
        # print("\n\n")
        # readline()

        sort!(advanced)
        while length(advanced) > 0
            current = popfirst!(advanced)
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
                        if length(workers) < N
                            push!(workers, v)
                        else
                            push!(q, v)
                        end
                    end
                end
            end
            sort!(workers)
        end
    end
    return i
end





print("part 1: ", traverse(make_nice(data)) * "\n\n")
print("part 2: ", traverse_timed(make_nice(data), 5, 60))