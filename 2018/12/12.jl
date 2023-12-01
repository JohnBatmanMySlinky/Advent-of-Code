function get_data()
    data = readlines("input.txt")
    input_state = replace(data[1], "initial state: " => "")

    notes = Dict{String, String}()
    for each in data[3:end]
        pattern, outcome = split(each, " => ")
        notes[pattern] = outcome
    end

    return input_state, notes
end

function project(input_state::String, T::Int64)
    original_length = length(input_state)
    lpad_size = 0
    for i in 1:T
        if input_state[end-4:end] != "....."
            rpad = "....."
        else
            rpad = ""
        end

        if input_state[1:5] != "....."
            lpad = "....."
            lpad_size += 5
        else
            lpad = ""
        end

        input_state = lpad * input_state * rpad
        new_state = String["." for x in 1:length(input_state)]
        for i in 4:(length(new_state)-3)
            pot = input_state[i-2:i+2]
            if pot ∈ keys(notes)
                new_state[i] = notes[pot]
            end
        end
        (i % 1 == 0) && print("$(i): $(input_state)\n")
        input_state = join(new_state)
        (i % 1 == 0) && print("$(i): $(input_state)\n")
        (i % 1 == 0) && print("$(i): $(calc_score(input_state, lpad_size))\n\n")
    end
    
    return calc_score(input_state, lpad_size)
end

function calc_score(input_state::String, lpad_size::Int64)::Int64
    score = 0
    for (idx, val) in enumerate(split(input_state, ""))
        if val == "#"
            score += idx - lpad_size - 1
        end
    end
    return score
end

input_state, notes = get_data()
score = project(input_state, 20)
print("part1: $(score)")


# print("\n\n\n")
# input_state, notes = get_data()
# score = project(input_state, 50_000_000_000)
# print("part1: $(score)")
