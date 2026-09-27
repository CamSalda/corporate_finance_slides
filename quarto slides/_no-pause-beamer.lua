-- Drop ". . ." pause markers when rendering to beamer, so a slide built up in
-- steps on screen prints as a single page in the PDF handout.
if not FORMAT:match("beamer") then
  return {}
end

local function is_pause(para)
  local c = para.content
  return #c == 5
    and c[1].t == "Str" and c[1].text == "."
    and c[3].t == "Str" and c[3].text == "."
    and c[5].t == "Str" and c[5].text == "."
end

return {
  { Para = function(el) if is_pause(el) then return {} end end },
}
