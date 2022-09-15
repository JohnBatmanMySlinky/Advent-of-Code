const data = readlines("input.txt")[1]

function react(s::String)::Tuple{Bool, String}
    for i in 1:(length(s)-1)
        if (s[i] == lowercase(s[i+1]))||(lowercase(s[i]) == s[i+1])
            if s[i] != s[i+1]
                return true, join([x for (j,x) in enumerate(s) if !(j∈[i,i+1])])
            end
        end
    end
    return false, s
end


function reaction(s::String)::Int64
    i = 0
    check = true
    while check == true
        i += 1
        check,s = react(s)
    end
    return length(s)
end

@time print("part 1: " * string(reaction(data)))

function part2loop(s::String)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_log = Dict{Char, Int64}()
    for letter in alphabet
        new_s = replace(s, letter=>"")
        new_s = replace(new_s, uppercase(letter)=>"")
        @time alphabet_log[letter] = reaction(new_s)
        print(string(letter) * " done!")
    end
    
    winner_val = 100000000
    winner_amt = 100000000
    for k in keys(alphabet_log)
        if alphabet_log[k] < winner_val
            winner_val = alphabet_log[k]
            winner_amt = k
        end
    end
    return winner_amt, winner_val
end

a, b = part2loop(data)
print(string(a) * " " * string(b))