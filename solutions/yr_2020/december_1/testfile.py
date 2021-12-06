from puzzle_input import tst_input


def find_entry_in_list(
    searching_nr: int,
    in_list: list,
    no_combine: int,
    cur_dpt: int = 0,
    nr_dict: dict = {},
    current_idx: int = -1,
):
    cur_dpt += 1
    # Making sure not to combine the same items when recursing
    for idx, item in enumerate(in_list):
        if current_idx == idx:
            # print(
            #     f"Not comparing idx: {current_idx} and {idx}, these are the same numbers!"
            # )
            pass
        else:
            nr_dict[cur_dpt] = item
            current_sum = sum(nr_dict.values())
            print(
                f"Currently on: {cur_dpt}, handling number: {item}, for dict: {nr_dict}, current sum: {current_sum}"
            )
            if cur_dpt < no_combine:
                return find_entry_in_list(
                    searching_nr=searching_nr,
                    in_list=in_list,
                    no_combine=no_combine,
                    cur_dpt=cur_dpt,
                    nr_dict=nr_dict,
                    current_idx=idx,
                )
            elif current_sum == searching_nr:
                print(f"Found it! {nr_dict}")
                return nr_dict
            else:
                nr_dict.pop(cur_dpt)

    # return nr_dict


print(find_entry_in_list(searching_nr=2020, in_list=tst_input, no_combine=2))
