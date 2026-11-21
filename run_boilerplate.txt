iverilog -g2012 -o tb_output.vcd -c logical/filelist -c sim/filelist_tb
vvp tb_output.vcd
gtkwave tb_output.vcd