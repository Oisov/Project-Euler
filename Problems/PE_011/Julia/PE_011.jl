function file_2_matrix(path="../Data/PE_011_data.txt")
    convert(Array{Int64}, readdlm(path))
end


function sublists_with_min_len(array, min_length)
    last_zero = 0
    sublists = []
    for (index, value) in enumerate(array)
        if value == 0
            if (index-1) - (last_zero) >= min_length
                push!(sublists, array[last_zero+1:index-1])
            end
            last_zero = index
        end
    end
    if last_zero == 0
        [array]
    else
        sublists
    end
end


function max_product_of_length_n(array, product_length=4)
    next_product = BigInt(prod(array[1:product_length]))
    max_product = next_product

    for index = 2:(length(array)-product_length+1)

        next_product = BigInt(prod(array[index:index+product_length-1]))
        if next_product > max_product
            max_product = next_product
        end

    end
    max_product
end


function max_line_sum(matrix, min_length)
    max_product = -Inf
    for index = 1:size(matrix, 1)
        for sublist in sublists_with_min_len(matrix[index, :], min_length)
            max_sublist_product = max_product_of_length_n(sublist, min_length)
            if max_sublist_product > max_product
                max_product = max_sublist_product
            end
        end
    end
    max_product
end


function max_diag_sum(mtx, min_length)
    max_product = -Inf
    for k = (-size(mtx, 1)+min_length):(size(mtx ,2)-min_length)
        for sublist in sublists_with_min_len(diag(mtx, k), min_length)
            max_sublist_product = max_product_of_length_n(sublist,
                                                          min_length)
            if max_sublist_product > max_product
                println(max_sublist_product)
                max_product = max_sublist_product
            end
        end
    end
    max_product
end


function PE_011(min_length = 4, matrix = file_2_matrix())
    max_vertical = max_line_sum(matrix, min_length)
    max_diagonal_1 = max_diag_sum(matrix, min_length)

    matrix_transposed = transpose(matrix)
    println("")
    max_horizontal = max_line_sum(matrix_transposed, min_length)
    max_diagonal_2 = max_diag_sum(matrix_transposed, min_length)

    max(max_vertical, max_diagonal_1, max_horizontal, max_diagonal_2)
end


println(PE_011())
