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
    pad = "....."
    for i in 1:T
        input_state = pad * input_state * pad
        new_state = String["." for x in 1:length(input_state)]
        for i in 4:(length(new_state)-3)
            pot = input_state[i-2:i+2]
            if pot ∈ keys(notes)
                new_state[i] = notes[pot]
            end
        end
        print("$(i): $(input_state)\n")
        input_state = join(new_state)
        print("$(i): $(input_state)\n\n")
    end
    
    score = 0
    for (idx, val) in enumerate(split(input_state, ""))
        if val ∈ ["#", '#']
            score += idx - length(pad) * T - 1
        end
    end
    return score
end

input_state, notes = get_data()
score = project(input_state, 20)
print("part1: $(score)")
