data = readlines("input.txt")

function part1(data::Vector{String})
    answer = 0
    for each in data
        answer += parse(Float64, each)
    end
    return answer
end

function part2(data::Vector{String})
    seen = Set(0)
    answer = 0
    while true
        for each in data
            answer += parse(Float64, each)
            answer ∈ seen && return answer
            push!(seen, answer)
        end
    end
end

print("part 1: " * string(part1(data)) * "\n")
print("part 2: " * string(part2(data)))