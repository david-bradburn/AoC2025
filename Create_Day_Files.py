
import os
import argparse
# from url import get_aoc_url


def get_boilerplate(boilerplate_name: str):
  boiler_plate_fd = open(f"{boilerplate_name}.txt", "r")

  boiler_plate_arr = boiler_plate_fd.readlines()
  boiler_plate_str = ""
  for line in boiler_plate_arr:
    boiler_plate_str += line
  return boiler_plate_str


def make_python_files(day_path_i, year, day, part):
  python_part_path = os.path.join(day_path_i, "python_src")
  os.mkdir(python_part_path)
  day_python_file_name = str(day) + "_" + str(part) + ".py"
  file_path  = os.path.join(python_part_path, day_python_file_name)
  f = open(file_path, "w")
  boiler_plate_str = get_boilerplate("python_day_boilerplate")
  boiler_plate = boiler_plate_str.format(year, day, day, part, year)
  f.write(boiler_plate)
  f.close()


def make_verilog_files(day_path_i, year, day, part):
  verilog_part_path = os.path.join(day_path_i, "verilog_src")
  verilog_logical = os.path.join(verilog_part_path, "logical")
  module_name = f"p{day}_{part}.sv"
  module_file_path = os.path.join(verilog_logical, module_name)
  os.mkdir(verilog_logical)
  with open(module_file_path, "w") as fd:
    boiler_plate_str = get_boilerplate("module_boilerplate")
    boiler_plate = boiler_plate_str.format(year, day, day, part)
    fd.write(boiler_plate)


  verilog_sim = os.path.join(verilog_part_path, "sim")
  tb_name = f"{module_name}_tb"
  tb_path = os.path.join(verilog_sim, tb_name)
  os.mkdir(verilog_sim)
  with open(tb_path, "w") as fd:
    boiler_plate_str = get_boilerplate("tb_boilerplate")
    boiler_plate = boiler_plate_str.format(year, day, day, part)
    fd.write(boiler_plate)



def create_folder(cur_wd, year: str, day: str, type=str):
  day_path = os.path.join(cur_wd, f"Day {day}", type)
  if not os.path.exists(day_path):
    os.mkdir(day_path)
    print(f"Created day {day} of AoC {year} {type}")
    return True
  print(f"Day {day} of AoC {year} {type} already exists")
  return False

def create_misc_area(day_str):
  misc_path = os.path.join(day_str, "misc")
  try:
    os.mkdir(misc_path)
  except FileExistsError:
    print("Misc file already exists")
    return

  test_path = os.path.join(misc_path, "test.txt")
  input_path = os.path.join(misc_path, "input.txt")

  f = open(test_path, "w")
  f.close()
  f = open(input_path, "w")
  f.close()


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("-y", "--year",
                      help="The year of AoC you want to create", type=str)
  parser.add_argument("-d", "--day",
                      help="The day of AoC you want to create", type=str)
  parser.add_argument("-p", "--pyth",
                      help="Create python folders",action="store_true")
  parser.add_argument("-v", "--veri",
                      help="Create verilog folders", action="store_true")
  parser.add_argument("-m", "--misc",
                      help="Create misc folders", action="store_true")
  args = parser.parse_args()
  day_no = args.day
  year_no = args.year
  python_cr = args.pyth
  verilog_cr = args.veri

  day_str = f"Day {day_no}"
  current_wd = os.getcwd()
  print(f"Creating {year_no} day {day_no}")
  if python_cr:
    python_cr = create_folder(current_wd, year_no, day_no, "python_src")
  if verilog_cr:
    verilog_cr = create_folder(current_wd, year_no, day_no, "verilog_src")

  if python_cr:
    make_python_files(day_str, year_no, day_no, 1)
    make_python_files(day_str, year_no, day_no, 2)

  if verilog_cr:
    make_verilog_files(day_str, year_no, day_no, 1)

  create_misc_area(day_str)


if __name__ == "__main__":
  main()
