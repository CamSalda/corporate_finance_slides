# The Finance and Economics Papers Podcast: Lecture Companion. Corporate Finance, Lecture 6: Estimating the Cost of Capital

> **Lecture companion.** This episode walks through Lecture 6 of the Corporate Finance course at ESCP Business
> School (Camilo Saldarriaga, 2026/2027), which covers chapter 12 of Berk and DeMarzo. It is made with the
> open-source tools of The Finance and Economics Papers Podcast, for the students of the course. All numbers
> and examples come from the lecture slides.

- **Lecture:** Corporate Finance, Lecture 6: Estimating the Cost of Capital. ESCP Business School, 2026/2027.
- **Textbook:** Berk, J., & DeMarzo, P. *Corporate Finance*, chapter 12.
- **Topics:** Recap of alpha and market efficiency; IRR and NPV; the CAPM recipe for the equity cost of capital; the market portfolio, the risk-free rate and the market risk premium; estimating beta by regression; the debt cost of capital, yield versus expected return, debt betas; a project's cost of capital, unlevering a comparable, net debt; industry asset betas, execution risk; the WACC; exercises
- **Length:** 32 minutes
- **Hosts:** Mei (the guide) and Miguel (the student)

## Cold open

MEI: Welcome to The Finance and Economics Papers Podcast, where we discuss the papers that shaped finance and economics, to make reading them easier and more fun. I'm Mei.

MIGUEL: And I'm Miguel. I'm the one who asks the questions you're too embarrassed to ask in class.

MEI: Today is a special format. Instead of a paper, we walk through a lecture: Lecture 6 of the Corporate Finance course at ESCP, "Estimating the Cost of Capital." It follows chapter 12 of the Berk and DeMarzo textbook, and every number we mention comes from the slides.

MIGUEL: Lecture six. Sixty-seven slides. I checked.

MEI: Sixty-seven slides, eight exercises, and a Dragon Ball theme park. This is the lecture where the theory finally touches a spreadsheet. Here's the plan from the first slide. Recap lecture five. How to measure the cost of money for a project. Build the CAPM recipe, one input at a time. Price the debt, then a non-traded project. And adjust for risk and financing: the WACC.

MIGUEL: Equations?

MEI: Many, but of a friendly kind: most of them are weighted averages and the CAPM formula applied again and again. Where the slides do algebra, the constant growth formula and the unlevering formulas, we give the intuition and point you to the slide. The exercises we do with numbers, all of them, because that's what the exam looks like.

MIGUEL: Recap first.

## Recap of lecture five

MEI: Two recap slides. The CAPM gives the return a stock must pay for its beta: the risk-free rate plus beta times the market risk premium. Alpha is the expected return minus that required return. Positive alpha, above the Security Market Line; negative, below. Under the CAPM every alpha is zero.

MIGUEL: And beating the market.

MEI: A positive alpha attracts buyers, the price rises, the expected return falls: competition pushes alphas back to zero. Every buyer needs a seller, so every positive alpha is someone else's negative alpha, and holding the market guarantees an alpha of zero. And yet, the survey of 392 chief financial officers: seventy-three point five percent use the CAPM, forty percent historical average returns, about a third a multifactor model. The box: the CAPM is simple and well founded, and the discount rate is only one imprecise input. Today we use it to compute the cost of capital.

## Some questions to start

MEI: The lecture opens with three questions. What is an investment project? What makes it different from ordinary spending? And: you are the manager of a big company and you want to execute a big investment project. How do you get the money?

MIGUEL: And then two examples from the news.

MEI: Example one. Headlines from August 2026: Paris courts Saudi investors to spend one billion euros on a "highly confidential" manga theme park. A Dragon Ball park near Paris, on the site of the defunct Mirapolis. The deal could exceed one billion euros.

MIGUEL: Professor Saldarriaga really went far on this one. A Dragon Ball theme park in a corporate finance lecture.

MEI: And he's right to. One billion euros: who pays, and what do they want back? That is the whole lecture in one question. Example two: the Tour Montparnasse, an eight hundred million euro renovation project, halted. Was the expected return worth what the money costs?

MIGUEL: So what is the lecture about?

MEI: Two ways to raise that money, and how to measure the cost of each. Equity: sell a share of the company to investors. Debt: borrow the money and pay it back with interest. First we evaluate their cost separately, then we see how companies combine them. And then you compare the cost of capital with the return the project is expected to earn. If the project earns less than the money costs, it's not worth doing. The definition in the box: the cost of capital is the return investors could earn elsewhere on an investment with the same risk.

## How a project is evaluated

MEI: Two slides on the two ways to judge a project, and they're a reminder from earlier in the program. A project costs an amount I today and pays a cash flow c at the end of each of the next N years.

MIGUEL: Way one.

MEI: Compute a return, then compare it with the cost of capital. Ask what return the project itself earns: the rate that makes the net present value zero. That's the internal rate of return, the IRR. The slide writes the NPV as minus the investment plus each cash flow discounted at the IRR. Accept the project when the IRR is above the cost of capital. The test is a rate against a rate.

MIGUEL: Way two.

MEI: Discount, then compare amounts. Don't compute the project's own return. Instead, discount every cash flow at the cost of capital and add them up: that's the present value. NPV is present value minus the investment. Accept when it's positive. Here the test is an amount against an amount. And the box: the two are equivalent. A return above the cost of capital is exactly what makes the discounted cash flows exceed the investment.

MIGUEL: Either way we need the cost of capital.

MEI: Either way we need it, and that's today. Outline, seven sections, all chapter 12. A, the equity cost of capital: the recipe. B, inputs one to three: the market portfolio, the risk-free rate, the premium. C, input four: beta. D, the debt cost of capital. E, a project's cost of capital. F, project risk and financing: the WACC. G, why we keep the CAPM.

## A. The recipe: the CAPM formula

MEI: Section A. The cost of capital of any investment is the expected return of the investments available in the market with the same beta. And the CAPM, from lecture four, tells us what that return is: the equity cost of capital equals the risk-free rate plus the equity beta times the market risk premium. The box: investors require the same risk premium they would earn by taking the same market risk through the market portfolio itself.

MIGUEL: Example 12.1.

MEI: Disney and Domino's Pizza. Disney: volatility twenty percent, beta one point two nine. Domino's: volatility thirty percent, beta zero point six two. Risk-free rate three percent, expected market return eight.

MIGUEL: So Domino's is riskier.

MEI: Total risk is volatility: Domino's, thirty against twenty. Market risk is beta: Disney, one point two nine against zero point six two. Now the cost of capital. Market premium: eight minus three, five percent. Disney: three plus one point two nine times five, nine point four five percent. Domino's: three plus zero point six two times five, six point one zero percent.

MIGUEL: The more volatile stock has the cheaper capital.

MEI: Because only market risk is paid for. The rest can be diversified away. Pizza demand doesn't move much with the business cycle.

MIGUEL: And the exercise, Saint-Gobain and ENGIE.

MEI: Same structure with French names. Saint-Gobain: volatility thirty percent, beta one point four five. ENGIE: volatility thirty-eight, beta zero point eight two. Total risk: ENGIE. Market risk: Saint-Gobain. Premium five percent. Saint-Gobain: three plus one point four five times five, ten point two five percent. ENGIE: three plus zero point eight two times five, seven point one zero percent. Same lesson: the more volatile stock, ENGIE, has the lower cost of capital.

MIGUEL: So the formula is easy.

MEI: The formula is easy. The work is in the inputs, and the slide lists four. The market portfolio. The risk-free rate. The market risk premium. And the beta. Sections B and C.

## B. Inputs 1 to 3

MEI: Input one, the market portfolio: every stock held in proportion to its market value. The market value of a firm is its market capitalization, number of shares times price per share, and a firm's weight is its market value over the market value of all firms together. Value-weighted.

MIGUEL: And the slide says value-weighted means passive.

MEI: Nice point. Holding every firm in proportion to its market value is the same as owning the same fraction of every firm: say zero point zero one percent of Nvidia, zero point zero one percent of LVMH, and so on. When prices move, the market weights move, but so does the value of what you hold, by exactly the same amount. No trading is needed to stay value-weighted. You only trade when a firm issues or buys back shares, or enters or leaves the market. So the market portfolio is cheap to hold, one reason it's the benchmark.

MIGUEL: In practice?

MEI: An index as proxy. The S&P 500: five hundred of the largest US firms, value-weighted. Only five hundred of some four thousand listed firms, but about eighty percent of the US market value. In Europe, the Euro Stoxx 50, the CAC 40, or a broad world index. You invest through an index fund or an ETF. And keep in mind: how well the CAPM works depends on how closely the proxy tracks the true market.

MIGUEL: Input two, the risk-free rate.

MEI: Taken from government bond yields. Which maturity? Match it to the investment: a short rate for a short project, a long rate for a long one. For a firm's cost of capital, most analysts use ten- to thirty-year bonds.

MIGUEL: Input three, the premium.

MEI: How much the market is expected to pay above the risk-free rate. It cannot be observed, so it has to be estimated, two ways. The historical approach: what the market actually paid over the risk-free rate in the past. The fundamental approach: the return that justifies today's index level, given what firms are expected to pay out. Same number seen from two ends.

MIGUEL: The historical table.

MEI: The average excess return of the S&P 500. Over one-year Treasuries: seven point seven percent from 1926 to 2015, five point zero from 1965 to 2015. Over ten-year Treasuries: five point nine and three point nine. Two patterns. Lower against ten-year bonds than against one-year bills, because long rates are usually higher than short rates. And lower since 1965: more people invest in stocks, diversifying is cheaper with funds and ETFs, and market volatility has fallen. Most analysts now use four to six percent over bills, three to five over long bonds.

MIGUEL: Drawbacks?

MEI: Imprecise, even since 1926 the margin of error is about plus or minus four percent, and backward looking.

MIGUEL: The fundamental approach.

MEI: Look forward. With the constant growth model from chapter 9, the expected return of the market is the dividend yield plus the expected dividend growth. Dividend yield: next year's dividend over today's index level. Example: dividend yield two percent, expected growth six, market return eight percent. Constant growth is a poor assumption for one firm, a reasonable one for the whole market. Studies using it find a premium of three to five percent.

MIGUEL: And there's a slide on where the formula comes from.

MEI: Here's our rule. The price of a stock is the present value of all its dividends. If each dividend is one plus g times the one before, and growth stays below the discount rate, the whole infinite sum collapses to next year's dividend divided by r minus g. Turn it around and you get r equals dividend yield plus g. Intuition: investors earn what the asset pays out today, plus the rate at which that payout grows. The step-by-step proof is in the appendix at the end of the deck, two slides, and it's a lovely piece of algebra: you call the infinite sum S, multiply by x, subtract, and everything cancels but a one. Go look at it once, it's the same trick behind every annuity formula you'll ever meet.

## C. Input 4: beta

MEI: Section C, the last input. Beta measures how much a stock moves when the market moves: a beta of two means a one percent move in the market comes with a two percent move in the stock, on average. From lecture two, it's the covariance of the stock with the market scaled by the variance of the market. Ideally we'd want the future beta. We can't see it, so we estimate it from past returns, which works because betas are fairly stable over time. Data providers use two to five years of weekly or monthly returns, with the S&P 500 or a local index as the market.

MIGUEL: Three steps.

MEI: Step one: look at the returns over time. Cisco's monthly returns against the S&P 500. Cisco moves in the same direction as the market, with bigger swings. Its beta is above one.

MIGUEL: Step two.

MEI: Plot the stock against the market. Each dot is one month: the market's excess return across, Cisco's up. Draw the best-fitting line. Its slope is the beta. The distance of each dot from the line is the diversifiable, firm-specific part of the return.

MIGUEL: Step three, the regression.

MEI: The best-fitting line comes from a linear regression, and the slide writes it as one line with three parts. Each month's excess return of the stock equals an intercept, plus beta times the market's excess return, plus a leftover. Beta is the slope, the part explained by the market, the number we want. The intercept is the stock's alpha from lecture five: how far its average return sat above or below the Security Market Line. The CAPM says it should be close to zero. And the leftover is firm-specific noise, zero on average: the diversifiable risk. One equation, and you've met every piece of it before.

## D. The debt cost of capital

MEI: A transition slide, "The cost of debt," and a picture of a balance sheet. Sections A to C priced the equity. A firm also borrows, and lenders expect a return too: the debt cost of capital. We'll need it to price a project in section E.

MIGUEL: Promised is not expected.

MEI: The key sentence of section D. The yield to maturity of a bond is the return an investor earns if every promised payment is made. If the borrower is very unlikely to default, the yield is a fine estimate of the expected return. If default is a real possibility, the yield is a promised return, and the expected return is lower: some of the time, the investor will not be paid in full. The box: using the yield as the cost of debt is a common mistake. It is only right for very safe debt.

MIGUEL: The one-year bond.

MEI: Invest one euro in a one-year bond with yield y. No default, with probability one minus p: you receive one plus y. Default, with probability p: you lose a fraction L of what was promised. The expected return is the average of the two, weighted by their probabilities, and it simplifies to y minus p times L. In words: the yield, minus the probability of default times the loss when it happens.

MIGUEL: How often does debt default?

MEI: A table from Moody's, 1920 to 2011. Average default rates by rating: triple A, zero. Double A, zero point one percent. Single A, zero point two. Triple B, zero point five. Double B, two point two. Single B, five point five. Triple C, twelve point two. Double C and below, fourteen point one. And in recessions those numbers jump: triple B three percent, double B eight, single B sixteen, triple C forty-eight, and the lowest tier seventy-nine percent.

MIGUEL: Seventy-nine percent in a recession.

MEI: Four out of five. That's why the lower part of the table is called junk.

MIGUEL: The second route.

MEI: Use the CAPM for debt: risk-free rate plus a debt beta times the market risk premium. But most bonds and all bank loans trade rarely, so a firm's own debt beta can't be estimated from returns. Instead, average debt betas by rating, from a Stanford working paper. A and above: below zero point zero five. Triple B: zero point one zero. Double B: zero point one seven. Single B: zero point two six. Triple C: zero point three one. By maturity, for investment grade: from zero point zero one at one to five years up to zero point one four beyond fifteen years. Debt betas are low, but they rise with lower ratings and longer maturities.

MIGUEL: Exercise: Lafarge.

MEI: January 2014. A Lafarge bond, coupon four point seven five percent, maturing September 2020, rated double B, yield to maturity three point seven percent. Expected loss rate sixty percent. Risk-free rate zero point six, market risk premium three point one. Estimate the expected return of Lafarge debt, both routes.

MIGUEL: Route one.

MEI: Yield minus expected loss. A double B bond defaults two point two percent of the time in a normal year, loss rate sixty percent. Three point seven minus two point two times zero point six, that's three point seven minus one point three two: two point three eight percent.

MIGUEL: Route two.

MEI: The CAPM. Average beta of double B debt, zero point one seven. Zero point six plus zero point one seven times three point one, that's zero point six plus zero point five three: one point one three percent.

MIGUEL: Two point three eight against one point one three. Those are quite different.

MEI: They are, and both are well below the three point seven percent yield, which is the lesson. The yield is the ceiling, not the expected return. The two routes are rough estimates from averages; in practice you'd report a range.

## E. A project is not traded

MEI: Section E, the heart of the lecture. A stock has a price history, so we can estimate its beta. A new project has none. So we borrow the beta of a comparable firm: a listed firm in the same business. Often that's the firm doing the project itself.

MIGUEL: Two cases.

MEI: Case one: the comparable has no debt. Its beta is the project's beta. Case two: the comparable has debt. We first have to unlever it. And one assumption in a box, which holds until section F: the firm pays for the project with shareholders' money only. The debt in case two belongs to the comparable firm; our project still uses none.

MIGUEL: Case one.

MEI: If the comparable has no debt, owning its shares is the same as owning its assets: all the cash the assets produce goes to the shareholders. So its equity beta is the beta of its assets, and we use it directly in the CAPM. Behind the formula: instead of doing the project, your investors could simply buy shares of the comparable. The project must offer at least that return.

MIGUEL: Exercise: 1000mercis.

MEI: You wish to launch a data marketing firm, using 1000mercis as the reference. 1000mercis has no debt and a beta of zero point five nine. Risk-free rate three percent, market risk premium five. Step one: no debt, so the asset beta is the equity beta, zero point five nine. Step two: three plus zero point five nine times five, five point nine five percent. A low beta, so a low bar: data marketing revenues don't swing much with the economy. Discount the business plan at about six percent.

MIGUEL: Case two.

MEI: The comparable has debt. There's a figure: the firm's assets on one side, debt and equity on the other. With debt, the cash the assets produce is split between lenders and shareholders. The shares alone are riskier than the assets, so the equity beta overstates the project's risk. To own the assets, you hold the debt and the equity together, and the risk of that combination is the risk of the assets.

MIGUEL: And this is where the formulas come.

MEI: Three slides, and here's the intuition that makes all three obvious. The firm's assets are owned by two groups: shareholders hold E of firm value, lenders hold D. Between them they own the whole business. Whatever the assets earn is shared out between those two groups, so the return on the assets is the average of what each group gets, weighted by the share of the firm each one holds. That's the unlevered cost of capital: E over E plus D times the equity cost, plus D over E plus D times the debt cost.

MIGUEL: And betas?

MEI: Betas combine exactly the same way, because the beta of a portfolio is the weighted average of the betas, lecture four. So the unlevered beta is the same weighted average of the equity beta and the debt beta. That is the project beta we were looking for, and then back to the recipe of section A. Two routes to the same number: average the returns, or average the betas and apply the CAPM.

MIGUEL: And the sentence to keep?

MEI: From the intuition slide: borrowing does not make the business itself any riskier. It only decides who carries that risk. Lenders take the safer part, low debt beta, so shareholders are left holding the riskier part, high equity beta. To find the risk of the underlying business, put the two pieces back together. That's what unlever means. The formulas are on the slides; once you've got this sentence, you can rebuild them yourself.

MIGUEL: Exercise: Danone.

MEI: A company wants to launch a new biscuit, and Danone is the comparable. Market cap thirty billion euros, equity beta zero point four. Debt ten billion, average yield three point five percent, default risk negligible. Risk-free rate three percent, market premium five.

MIGUEL: Step by step.

MEI: Step one, equity cost of capital: three plus zero point four times five, five percent. Step two, debt cost: negligible default risk, so the yield, three point five percent. Step three, weights: E plus D is forty; equity thirty over forty, seventy-five percent; debt twenty-five. Step four, average the returns: zero point seven five times five plus zero point two five times three point five, that's three point seven five plus zero point eight seven five: four point six two five percent.

MIGUEL: Or average the betas.

MEI: With a debt beta of zero: zero point seven five times zero point four, zero point three zero. Then three plus zero point three times five: four point five percent. So the biscuit project should be discounted at about four and a half to four point six percent. A safe, low-beta business. People buy biscuits in recessions too.

MIGUEL: Why don't the two routes agree exactly?

MEI: Because route one uses the yield, three point five percent, as the cost of debt, while route two uses a debt beta of zero, which implies a cost of debt equal to the risk-free rate, three percent. Negligible default risk in one, exactly zero in the other. Small gap, same answer for the business plan.

## Cash is negative debt

MEI: One refinement. Many firms hold more cash than they need. Cash is a risk-free asset sitting on the balance sheet, and it makes the firm's shares safer than its actual business. If a firm holds one euro of cash and owes one euro of risk-free debt, the two cancel. So we measure leverage with net debt: debt minus excess cash. Use net debt in place of D in the unlevering formulas. And if a firm has more cash than debt, net debt is negative, and the beta of its business ends up above its equity beta.

MIGUEL: Exercise: Accenture.

MEI: End of 2010. Accenture: market cap twenty-five billion euros, no debt, four billion in cash, equity beta one. Estimate the beta of its assets. Step one, net debt: zero minus four, minus four billion. Step two, the value of the business: twenty-five minus four, twenty-one. Step three, unlever with cash risk-free: twenty-five over twenty-one times one, plus minus four over twenty-one times zero. One point one nine.

MIGUEL: So the consulting business is riskier than the shares.

MEI: One point one nine against one point zero. The cash dilutes the risk the shareholders see. Strip it out and the business underneath is more cyclical than the stock suggests.

## Industry asset betas and project risk

MEI: A figure from the textbook: median and quartiles of asset betas by industry in the US. Companies very sensitive to the market and the economy have high betas; stable or counter-cyclical ones have low betas. Cyclical: construction, car manufacturing, technology. Stable: utilities, household products. Counter-cyclical: gold mines, education.

MIGUEL: Education is counter-cyclical?

MEI: When the job market is bad, people go back to school. Good news for business schools, and for the professor. And a warning on the slide: cyclical does not mean volatile. Film producers have very risky cash flows, but those cash flows have a low correlation with market returns. High volatility, low beta.

MIGUEL: Conglomerates.

MEI: A firm's asset beta reflects the market risk of its average project. For a conglomerate, identify a set of pure play comparables for each division, to estimate divisional or project-specific costs of capital. And operating leverage: the proportion of fixed costs relative to variable costs. More fixed costs, higher project beta, other things equal.

MIGUEL: The common mistake.

MEI: Execution risk. A new product can fail because of delays or marketing mistakes. Firms are tempted to punish that with a higher discount rate. That's wrong. Execution risk is firm-specific, so diversifiable, and the cost of capital only pays for market risk. Put it in the cash flows instead. A project expected to pay a hundred next year, with a twenty percent chance of paying nothing, has an expected cash flow of eighty. Discount eighty at the unchanged cost of capital. The box: risk that can be diversified goes into the expected cash flows, never into the discount rate.

## F. Project risk and financing: the WACC

MEI: Section F. So far we assumed the project was financed with equity only. Now drop that: what if the firm borrows to finance it? The slide announces two scenarios for the next lecture. In perfect capital markets, no taxes, no transaction costs: nothing changes. With corporate taxes: debt gets cheaper for the firm, and the project's cost of capital falls with it.

MIGUEL: The WACC.

MEI: The weighted average cost of capital, the cost of capital when equity and debt are combined to finance the project. It's the same weighted average as the unlevered cost, with one change: the debt cost is multiplied by one minus the corporate tax rate, because interest is tax-deductible. The next slide rewrites it: the WACC equals the unlevered cost of capital minus the debt weight times the tax rate times the cost of debt. In words: the unlevered cost of capital, minus the tax saving on the debt. Which is why the unlevered cost is also called the pre-tax WACC.

MIGUEL: Which one do you use?

MEI: There's a table. The unlevered cost is the return investors require to hold the firm's assets; use it for a project with the same risk as the firm, financed with equity only. The WACC is the after-tax cost of capital to the firm; use it for a project with the same risk and the same debt mix as the firm. The WACC is lower, by the tax saving on interest. Lectures nine and ten come back to how much debt a firm should carry and what the tax saving is really worth.

MIGUEL: Exercise: Michelon.

MEI: Michelon, with an o. Market cap one hundred million euros, debt twenty-five million. Equity cost of capital ten percent, cost of debt six. Corporate tax rate thirty-three percent. Unlevered cost and WACC?

MIGUEL: Steps.

MEI: Step one, weights: equity one hundred over one twenty-five, eighty percent; debt twenty percent. Step two, unlevered cost: zero point eight times ten plus zero point two times six, that's eight plus one point two: nine point two percent. Step three, the WACC, long form: zero point eight times ten, plus zero point two times six times one minus zero point three three. Eight plus zero point eight zero: eight point eight zero percent. Check with the short form: nine point two minus zero point two times zero point three three times six, nine point two minus zero point four zero: eight point eight zero. Same number. The slide adds that it's the same firm as the textbook's Dunlap example with a higher tax rate, so a bigger tax saving and a lower WACC, eight point eight against eight point nine.

MIGUEL: So borrowing lowers the discount rate by forty basis points.

MEI: Only because of taxes. Without taxes, the two numbers would be the same nine point two, which is the perfect-markets scenario the next lecture starts with.

## G. Conclusion about the use of the CAPM

MEI: Section G. Limitations: betas are unobservable, expected returns are unobservable, and the market index is not the true market portfolio. Advantages: revenue and cash flow projections are far more speculative than the cost of capital estimate; it's practical and straightforward; and it brings discipline and rigor.

MIGUEL: What to remember.

MEI: Five lines. The recipe: equity cost equals risk-free rate plus beta times the market premium, with the risk-free rate from long government bonds, a premium of three to five percent, and the beta from a regression. Yield is not the cost of debt: yield minus default probability times loss rate, or the CAPM with a debt beta by rating. A project has no beta of its own: unlever a comparable, with net debt for D. The WACC is the unlevered cost minus the tax saving on debt, for projects with the firm's risk and the firm's debt mix. And the discount rate is the least uncertain input of an NPV. Spend your worry on the cash flows.

## Wrap-up: the recap

MEI: Lecture six in one minute. A project costs money today and pays later; judge it by IRR against the cost of capital, or by NPV, and both agree. The cost of capital is what investors could earn elsewhere at the same risk. For equity, the CAPM: risk-free rate plus beta times the market premium. Disney nine point four five, Domino's six point one zero; Saint-Gobain ten point two five, ENGIE seven point one zero. The more volatile stock can have the cheaper capital.

MIGUEL: The inputs.

MEI: A value-weighted index as the market, a long government bond as the risk-free rate, a premium of three to five percent from history or from dividend yield plus growth, and a beta from the slope of a regression of the stock's excess returns on the market's.

MIGUEL: Debt.

MEI: The yield is a promise. Expected return is yield minus default probability times loss rate, or a debt beta by rating. Lafarge: two point three eight or one point one three, both well under the three point seven yield.

MIGUEL: Projects.

MEI: Borrow a comparable's beta. No debt: use it directly, 1000mercis at five point nine five. With debt: unlever, average equity and debt weighted by value, Danone at about four and a half. Use net debt: Accenture's business beta is one point one nine, above its stock's one. Execution risk goes into the cash flows, never into the rate. With taxes, the WACC is the unlevered cost minus the tax saving: Michelon, nine point two and eight point eight.

MIGUEL: The quiz.

MEI: Three inputs for the equity cost of capital: the risk-free rate from long government bonds, the market risk premium from history or dividend yield plus growth, and the beta from the regression slope. Why the yield overstates the cost of debt: it assumes every promised payment is made, and with default risk some won't be. Why the equity beta of a levered firm differs from its asset beta: debt takes the safer part of the cash flows, so equity carries more risk than the assets, and a project is like the assets, so unlever first. When to use the WACC: when the project has the same market risk and the same debt mix as the firm; otherwise start from the unlevered cost.

MIGUEL: My takeaway: the discount rate is a four-step recipe, and the step everyone gets wrong is forgetting to unlever. Also, if a Dragon Ball park opens near Paris, someone at ESCP computed its WACC, and I want to meet them.

MEI: Read chapter 12, redo Danone and Michelon with the slides closed, and look once at the appendix on the constant growth formula. Thanks for listening to The Finance and Economics Papers Podcast.

MIGUEL: See you in the next lecture.
