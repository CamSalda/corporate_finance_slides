// Reproduces the look of the online test: sans font, blue instruction text,
// white answer boxes, thin grey separators, radio buttons, question cards.
#set page(paper: "a4", margin: (x: 2cm, y: 2cm))
#set text(font: ("Segoe UI", "Arial"), size: 11pt, fill: rgb("#222222"))
#set par(leading: 0.85em)

#let blue = rgb("#2a7ab0")
#let grey = rgb("#e0e0e0")
#let rule = line(length: 100%, stroke: 0.5pt + grey)
#let ansbox = box(width: 2.2em, height: 2.2em, stroke: 0.8pt + rgb("#aaaaaa"), radius: 3pt, baseline: 45%)
#let radio = box(width: 1.1em, height: 1.1em, stroke: 1.2pt + rgb("#999999"), radius: 50%, baseline: 22%)
#let dropdown = box(inset: (x: 0.6em, y: 0.4em), stroke: (bottom: 1.5pt + blue), fill: rgb("#f7f7f7"), baseline: 35%)[
  #text(weight: "bold")[Select] #h(0.6em) #text(fill: blue, size: 8pt)[▼]
]
#let instr(body) = text(fill: blue)[#body]
#let pct = [#ansbox %.]
#let num = [#ansbox .]

#let question(n, parts, body) = [
  #block(width: 100%, stroke: 0.6pt + rgb("#cccccc"), radius: 3pt, inset: 0pt)[
    #block(width: 100%, inset: (x: 1.4em, y: 1em))[
      #text(weight: "bold", size: 15pt)[Question #n] \
      #text(size: 9pt, fill: rgb("#444444"))[#parts parts #h(0.5em) #box(line(angle: 90deg, length: 0.9em, stroke: 0.5pt + grey)) #h(0.5em) -- of 1 point]
    ]
    #line(length: 100%, stroke: 0.6pt + rgb("#cccccc"))
    #block(width: 100%, inset: (x: 1.4em, y: 1em))[#body]
  ]
  #v(1.2em)
  #text(weight: "bold", size: 14pt)[#underline[Review Only]]
  #v(0.8em)
  #rule
  #v(0.6em)
  #block(fill: rgb("#f3f4ef"), inset: (x: 1em, y: 0.8em))[
    #text(fill: blue)[#underline[View the Worked Solution (Formula Use).]]
  ]
]

#let part(n, total, body) = block(breakable: false, width: 100%)[
  #v(1.2em)
  #text(weight: "bold", size: 12.5pt)[Part #n of #total]
  #v(0.6em)
  #rule
  #v(0.6em)
  #body
]
#let choice(letter, body) = [#radio #h(0.8em) #letter. #h(0.5em) #body]
#let twodp = instr[(Enter your answer as a percentage and round it to two decimal places.)]
#let fivedp = instr[(Round your answer to five decimal places.)]

// =========================================================================
// QUESTION 1
// =========================================================================
#question(1, 6)[
  Arbor Systems and Gencore stocks both have a volatility of 43%. Compute the
  volatility of a portfolio with 50% invested in each stock if the correlation
  between the stocks is *(a)* +1.00, *(b)* 0.50, *(c)* 0.00, *(d)* −0.50, and
  *(e)* −1.00. In which of the cases is the volatility lower than that of the
  original stocks?
]

#let q1(n, rho) = part(n, 6)[
  If the correlation is #rho, the volatility of the portfolio is #twodp #pct
]
#q1(1, [+1.00])
#q1(2, [0.50])
#q1(3, [0.00])
#q1(4, [−0.50])
#q1(5, [−1.00])

#part(6, 6)[
  In which of the cases is the volatility lower than that of the original stocks?
  #instr[(Select the best choice.)]
  #v(0.8em)
  #set par(leading: 1.3em)
  #choice("A", [In all of the cases.]) \
  #choice("B", [In cases *(b)*, *(c)*, *(d)* and *(e)*.]) \
  #choice("C", [In cases *(d)* and *(e)*.]) \
  #choice("D", [In none of the cases.])
]

#pagebreak()

// =========================================================================
// QUESTION 2
// =========================================================================
#question(2, 14)[
  Using the data in the following #text(fill: blue)[#underline[table]], consider a
  portfolio that maintains a 70% weight on stock A and a 30% weight on stock B.
  #set enum(numbering: "a.", indent: 1em)
  + What is the return each year of this portfolio?
  + Based on your results from part *(a)*, compute the average return and volatility of the portfolio.
  + Show that (i) the average return of the portfolio is equal to the (weighted) average of
    the average returns of the two stocks, and (ii) the volatility of the portfolio equals
    the same result as from the calculation in Eq. 11.8.
  + Explain why the portfolio has a lower volatility than the average volatility of the two stocks.
]

#v(1.2em)
#text(weight: "bold", size: 13pt)[Data Table]
#v(0.6em)
#block(width: 100%, stroke: 0.6pt + rgb("#cccccc"), radius: 3pt, inset: (x: 1.4em, y: 1em))[
  #instr[(Click on the following #underline[link] in order to copy its contents into a spreadsheet.)]
  #v(0.4em)
  #table(
    columns: 7,
    stroke: none,
    inset: (x: 0.9em, y: 0.35em),
    align: (col, row) => if col == 0 { left + horizon } else { center + horizon },
    [*Year*], [*2010*], [*2011*], [*2012*], [*2013*], [*2014*], [*2015*],
    table.hline(stroke: 0.8pt + rgb("#555555")),
    [*Stock A*], [−8%], [12%], [10%], [−8%], [5%], [6%],
    [*Stock B*], [19%], [16%], [4%], [−7%], [−6%], [28%],
    table.hline(stroke: 0.8pt + rgb("#555555")),
  )
]

#part(1, 13)[
  *a.* What is the return each year of this portfolio?

  Enter the return of this portfolio for each year in the table below:
  #instr[(Enter your answers as percentages and round them to two decimal places.)]
  #v(0.4em)
  #table(
    columns: (auto, 1fr, 1fr, 1fr, 1fr, 1fr, 1fr),
    stroke: none,
    inset: (x: 0.6em, y: 0.7em),
    align: left + horizon,
    [*Year*], [*2010*], [*2011*], [*2012*], [*2013*], [*2014*], [*2015*],
    table.hline(stroke: 0.8pt + rgb("#555555")),
    [*Portfolio*], [#ansbox %], [#ansbox %], [#ansbox %], [#ansbox %], [#ansbox %], [#ansbox %],
    table.hline(stroke: 0.8pt + rgb("#555555")),
  )
]

#part(2, 13)[
  *b.* Based on your results from part *(a)*, compute the average return and volatility of the portfolio.

  The average return of the portfolio is #twodp #pct
]

#part(3, 13)[
  The variance of the portfolio is #fivedp #num
]

#part(4, 13)[
  The standard deviation of the portfolio is #twodp #pct
]

#part(5, 13)[
  *c.* Show that (i) the average return of the portfolio is equal to the (weighted) average of
  the average returns of the two stocks, and (ii) the volatility of the portfolio equals the
  same result as from the calculation in Eq. 11.8.

  The average annual return for stock A is #twodp #pct
]

#part(6, 13)[
  The average annual return for stock B is #twodp #pct
]

#part(7, 13)[
  The (weighted) average of the average returns of the two stocks is #twodp #pct
]

#part(8, 13)[
  The standard deviation of stock A is #fivedp #num
]

#part(9, 13)[
  The standard deviation of stock B is #fivedp #num
]

#part(10, 13)[
  The covariance between the stocks is #fivedp #num
]

#part(11, 13)[
  The variance of the portfolio is #fivedp #num
]

#part(12, 13)[
  The volatility of the portfolio is #twodp #pct
]

#part(13, 13)[
  *d.* Explain why the portfolio has a lower volatility than the average volatility of the two stocks.

  #set par(leading: 1.2em)
  The portfolio has a #instr[(Select your answer from the drop-down menu.)] #dropdown
  volatility than the average volatility of the two stocks because some of the idiosyncratic
  risk of the stocks in the portfolio is diversified away.
]

#pagebreak()

// =========================================================================
// QUESTION 3
// =========================================================================
#question(3, 9)[
  You own three stocks: 600 shares of Apple Computer, 10,000 shares of Cisco System, and
  5,000 shares of Colgate-Palmolive. The current share prices and expected returns of Apple,
  Cisco, and Colgate-Palmolive are, respectively, \$482, \$16, \$101 and 12%, 10%, 8%.
  #set enum(numbering: "a.", indent: 1em)
  + What are the portfolio weights of the three stocks in your portfolio?
  + What is the expected return of your portfolio?
  + Suppose the price of Apple stock goes up by \$28, Cisco rises by \$4, and Colgate-Palmolive
    falls by \$15. What are the new portfolio weights?
  + Assuming the stocks' expected returns remain the same, what is the expected return of the
    portfolio at the new prices?
]

#part(1, 8)[
  *a.* What are the portfolio weights of the three stocks in your portfolio?

  The portfolio weight of Apple is #twodp #pct
]

#part(2, 8)[
  The portfolio weight of Cisco is #twodp #pct
]

#part(3, 8)[
  The portfolio weight of Colgate-Palmolive is #twodp #pct
]

#part(4, 8)[
  *b.* What is the expected return of your portfolio?

  The expected return on the portfolio is #twodp #pct
]

#part(5, 8)[
  *c.* Suppose the price of Apple stock goes up by \$28, Cisco rises by \$4, and
  Colgate-Palmolive falls by \$15. What are the new portfolio weights?

  The new portfolio weight of Apple is #twodp #pct
]

#part(6, 8)[
  The new portfolio weight of Cisco is #twodp #pct
]

#part(7, 8)[
  The new portfolio weight of Colgate-Palmolive is #twodp #pct
]

#part(8, 8)[
  *d.* Assuming the stocks' expected returns remain the same, what is the expected return of
  the portfolio at the new prices?

  The new expected return is #twodp #pct
]

#pagebreak()

// =========================================================================
// QUESTION 4
// =========================================================================
#question(4, 3)[
  Suppose Johnson & Johnson and Walgreens Boots Alliance have expected returns and
  volatilities shown #text(fill: blue)[#underline[here]] with a correlation of 16%.
  Calculate *(a)* the expected return and *(b)* the volatility (standard deviation) of a
  portfolio that consists of a long position of \$9,500 in Johnson & Johnson and a short
  position of \$2,000 in Walgreens.
]

#let twodp1 = instr[(Enter your answer as a percentage and round it to two decimal place.)]

#part(1, 2)[
  *a.* Calculate the expected return of a portfolio that consists of a long position of
  \$9,500 in Johnson & Johnson and a short position of \$2,000 in Walgreens.

  The expected return of the portfolio is #twodp1 #pct
]

#part(2, 2)[
  *b.* Calculate the volatility (standard deviation) of a portfolio that consists of a long
  position of \$9,500 in Johnson & Johnson and a short position of \$2,000 in Walgreens.

  The volatility of the portfolio is #twodp1 #pct
]

#pagebreak()

// =========================================================================
// QUESTION 5
// =========================================================================
#question(5, 4)[
  Suppose Intel's stock has an expected return of 22% and a volatility of 32%, while
  Coca-Cola's has an expected return of 9% and volatility of 19%. If these two stocks were
  perfectly negatively correlated (i.e., their correlation coefficient is −1),
  #set enum(numbering: "a.", indent: 1em)
  + Calculate the portfolio weights that remove all risk.
  + If there are no arbitrage opportunities, what is the risk-free rate of interest in this economy?
]

#part(1, 3)[
  *a.* Calculate the portfolio weights that remove all risk.

  The portfolio weight of Intel would be #twodp #pct
]

#part(2, 3)[
  The portfolio weight of Coca-Cola would be #twodp #pct
]

#part(3, 3)[
  *b.* If there are no arbitrage opportunities, what is the risk-free rate of interest in this economy?

  The risk-free rate of interest in this economy is #twodp #pct
]
