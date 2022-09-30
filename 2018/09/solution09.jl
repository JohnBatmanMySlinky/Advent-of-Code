# data = [parse(Int64,x) for x in split(readlines("input.txt")[0]," ")]


function play(board::Vector{Int64}, N::Int64, cap::Int64)
    scores = Dict{Int64, Int64}()
    n = 0
    new_marble = 0
    while true
        n = mod(n,N)
        previous_idx = argmax(board)
        new_marble = maximum(board) + 1
        L = length(board)
        if mod(new_marble,23) == 0
            new_score = new_marble
            if previous_idx <= 7
                pop_idx = L + previous_idx - 7
            else
                pop_idx = previous_idx - 7
            end 
            new_score += board[pop_idx]
            deleteat!(board, pop_idx)
            previous_idx = pop_idx
            new_marble += 1
            L = length(board)

            if n in keys(scores)
                scores[n] += new_score
            else
                scores[n] = new_score
            end
        end

        if new_marble > cap
            break
        end
        
        if previous_idx + 2 <= L
            new_idx = previous_idx + 2
            insert!(board, new_idx, new_marble)
        elseif previous_idx + 2 == L+1
            push!(board, new_marble)
        else
            new_idx = previous_idx + 2 - L
            insert!(board, new_idx, new_marble)
        end
        # print(n, ": ", board, "\n")
        # readline()
        n += 1
    end
    return findmax(scores)
end

print(play([0], 431, 70950))