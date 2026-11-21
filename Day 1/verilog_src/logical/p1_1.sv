//
// https://adventofcode.com/2025/day/1
//

module p1_1 (
  input wire clk,
  input wire resetn,

  output wire cnt;
);

logic [31:0] cnt_i;

assign cnt = cnt_i;

always_ff @(posedge clk) begin
  if(!resetn) begin
    cnt_i <= '0;
  end else begin
    cnt_i <= cntcnt_i + 1'b1;
  end
end

endmodule