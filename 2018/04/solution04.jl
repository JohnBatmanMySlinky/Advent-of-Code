using Dates

lines = readlines("input.txt")

function SORT(s::Vector{String})
    tmp = []
    for line in lines
        time = match(r"\[.+\]", line).match
        time = replace(time, "[" => "")
        time = replace(time, "]" => "")
        time = DateTime(time, "yyyy-mm-dd HH:MM")
        push!(tmp, (time, line))
    end
    tmp = sort(tmp, by=first)
    return [x[2] for x in tmp]
end

function make_nice(s::String)::Tuple{Bool, Int}
    guard_number = match(r"#\d+", s)
    if guard_number == nothing
        time = match(r":\d\d\]", s).match
        time = replace(time, ":" => "")
        time = replace(time, "]" => "")
        return false, parse(Int, time)
    else
        return true, parse(Int, replace(guard_number.match, "#" => ""))
    end
end

function create_universe(dat::Vector{String})::Dict
    timesheet = []
    next_idx = (0, 0)
    # (day, guard#) => [(start, stop), (start, stop), ...]
    universe = Dict{Tuple{Int64, Int64}, Array{Int64}}()
    i = 0
    for line in dat
        guard_check, parsed = make_nice(line)
        if guard_check == true
            if length(timesheet) > 0 
                universe[next_idx] = timesheet
            end
            i += 1
            next_idx = (i, parsed)
            timesheet = []
        else
            push!(timesheet, parsed)
        end
    end
    universe[next_idx] = timesheet
    return universe
end

function most_minutes_asleep(d::Dict)
    sleep_log = Dict{Int64, Int64}()
    for (id, guard) in keys(d)
        timesheet = d[(id, guard)]
        sleep = 0
        for i in 1:length(timesheet)
            if isodd(i)
                sleep -= timesheet[i]
            else
                sleep += timesheet[i]
            end
        end
        if guard ∈ keys(sleep_log)
            sleep_log[guard] += sleep
        else
            sleep_log[guard] = sleep
        end
    end
    return findmax(sleep_log)
end

function find_most_slept_minute(D::Dict, chosen_guard::Int64)
    d = deepcopy(D)
    minute_log = Dict{Int64, Int64}()
    for (id, guard) in keys(d)
        if guard == chosen_guard
            timesheet = d[(id, guard)]
            while length(timesheet) > 0
                left = popfirst!(timesheet)
                right = popfirst!(timesheet)
                for i in left:(right-1)
                    if i ∈ keys(minute_log)
                        minute_log[i] += 1
                    else
                        minute_log[i] = 1
                    end
                end
            end
        end
    end
    return findmax(minute_log)[2]
end

function find_most_slept_minute2(d::Dict)
    minute_log = Dict{Int64, Dict{Int64, Int64}}()
    for (id, guard) in keys(d)
        if !(guard ∈ keys(minute_log))
            minute_log[guard] = Dict{Int64, Int64}()
        end
        timesheet = d[(id, guard)]
        while length(timesheet) > 0
            left = popfirst!(timesheet)
            right = popfirst!(timesheet)
            for i in left:(right-1)
                if i ∈ keys(minute_log[guard])
                    minute_log[guard][i] += 1
                else
                    minute_log[guard][i] = 1
                end
            end
        end
    end

    winner_minutes = 0
    winner_instance = 0
    winner_guard = 0
    for guard in keys(minute_log)
        a, b = findmax(minute_log[guard])
        if a > winner_instance
            winner_instance = a
            winner_minutes = b
            winner_guard = guard        
        end
    end
    return winner_guard * winner_minutes
end

sorted_lines = SORT(lines)
universe = create_universe(sorted_lines)
minutes_slept, chosen_guard  = most_minutes_asleep(universe)
most_slept_minute = find_most_slept_minute(universe, chosen_guard)
print("part 1: " * string(chosen_guard * most_slept_minute) * "\n")
print("part 2: " * string(find_most_slept_minute2(universe)))
