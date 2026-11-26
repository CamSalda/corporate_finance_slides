# The Finance and Economics Papers Podcast: Lecture Companion. Corporate Finance, Lecture 7: Capital Structure in a Perfect Market (I)

> **Lecture companion.** This episode walks through Lecture 7 of the Corporate Finance course at ESCP Business
> School (Camilo Saldarriaga, 2026/2027), which covers chapters 14.1 and 14.2 of Berk and DeMarzo. It is made
> with the open-source tools of The Finance and Economics Papers Podcast, for the students of the course. All
> numbers and examples come from the lecture slides.

- **Lecture:** Corporate Finance, Lecture 7: Capital Structure in a Perfect Market (I). ESCP Business School, 2026/2027.
- **Textbook:** Berk, J., & DeMarzo, P. *Corporate Finance*, chapters 14.1-14.2.
- **Topics:** Recap of the cost of capital; what CFOs think matters; Modigliani and Miller; one project financed with equity only, then with debt; levered equity and the common fallacy; the perfect capital market; MM Proposition I; homemade leverage and the arbitrage proof; the market value balance sheet
- **Length:** 26 minutes
- **Hosts:** Mei (the guide) and Miguel (the student)

## Cold open

MEI: Welcome to The Finance and Economics Papers Podcast, where we discuss the papers that shaped finance and economics, to make reading them easier and more fun. I'm Mei.

MIGUEL: And I'm Miguel. I'm the one who asks the questions you're too embarrassed to ask in class.

MEI: Today is a special format. Instead of a paper, we walk through a lecture: Lecture 7 of the Corporate Finance course at ESCP, "Capital Structure in a Perfect Market, part one." It follows chapters 14.1 and 14.2 of the Berk and DeMarzo textbook, and every number we mention comes from the slides.

MIGUEL: Lecture seven. The course changes gear here, doesn't it?

MEI: It does. Six lectures on what things are worth and what return they must pay. From today, the question is how a firm should pay for its projects: with the shareholders' money, with borrowed money, or a mix. Here's the plan from the first slide. Recap lecture six. Ask whether financing a project with debt or with equity changes what it's worth. Follow one entrepreneur who finances the same project two ways, and see why debt makes the equity riskier. Meet Modigliani and Miller's first proposition and the arbitrage behind it. And read a market value balance sheet.

MIGUEL: Equations?

MEI: Light. One example carried through the whole deck with small round numbers, and a proof made of two tables. Where the slides do algebra, we give the idea and point you to the slide. Today is mostly a story, and it's a good one.

MIGUEL: Recap first.

## Recap of lecture six

MEI: Five recap slides. The investment decision: a project is worth doing when its expected return is at least its cost of capital, the return investors could earn elsewhere at the same risk. The money comes from equity, debt, or a mix, and each has its own cost because each investor bears a different risk.

MIGUEL: The cost of equity.

MEI: The CAPM: risk-free rate plus beta times the market risk premium. The market portfolio is an index, the risk-free rate a long government bond, the premium three to five percent, the beta a regression slope.

MIGUEL: The cost of debt.

MEI: The yield is a promised return. With default risk, the expected return is the yield minus the probability of default times the loss rate. Or the CAPM with a debt beta by rating, near zero for investment grade, up to zero point three for the riskiest.

MIGUEL: A project's cost of capital.

MEI: A project has no beta of its own, so borrow one from a comparable. Without debt, use its equity beta directly. With debt, unlever: the assets belong to shareholders and lenders together, so the asset cost of capital, and the asset beta, are the weighted averages of the two. Cash counts as negative debt.

MIGUEL: And the WACC.

MEI: With taxes, interest is deductible, so the effective cost of debt is the cost of debt times one minus the tax rate, and the WACC is the weighted average with that adjustment. Without the tax term, it's the unlevered cost of capital, the pre-tax WACC. Hold on to that formula: today's first move is to switch the tax off.

## Introduction: CFOs, Modigliani and Miller

MEI: The transition slide frames the day. Lecture six measured the cost of equity and the cost of debt, and debt looked cheaper. Today we ask whether borrowing more therefore makes a firm worth more.

MIGUEL: And the first slide is a survey.

MEI: CFOs were asked which finance functions add the most value to the firm, Servaes and Tufano, 2006. At the top of the chart: capital structure. Then debt issuance and management, working capital, bank relationships, tax. Investment decisions come sixth. At the bottom: dividend policy, equity issuance, pension management. Capital structure is the mix of debt and equity a firm uses to finance its assets, and CFOs put it first.

MIGUEL: Which makes what comes next a little awkward.

MEI: Which makes what comes next delicious, because the two gentlemen on the next slide proved that, in a perfect world, capital structure doesn't matter at all. Franco Modigliani, 1918 to 2003, Nobel prize 1985. Merton Miller, 1923 to 2000, Nobel prize 1990. The paper: "The Cost of Capital, Corporation Finance and the Theory of Investment," American Economic Review, 1958.

MIGUEL: Two Nobel prizes for saying something doesn't matter.

MEI: Two Nobel prizes for saying exactly when it doesn't matter, which tells you exactly where to look when it does. And notice the tension the professor sets up on purpose: the CFOs say capital structure is the most valuable thing they do, and the theory says that in a frictionless world it's worth nothing. Both can be true. The CFOs live in a world with taxes, bankruptcy and information problems. MM describe the world without them. The gap between the two is the rest of the course.

MIGUEL: So the theorem is the baseline, and the frictions are the story.

MEI: Exactly. Their two propositions cover what leverage does to the value of the firm, that's today, Proposition I, and to the cost of equity and the cost of capital, Proposition II, lecture eight. The slide lists the uses: optimizing the capital structure, choosing the discount rate for a project, understanding how financing can change firm value.

MIGUEL: Outline.

MEI: Five sections. A, financing a project with equity. B, adding debt: levered equity and a common fallacy. C, perfect markets and MM Proposition I. D, homemade leverage and arbitrage. E, the market value balance sheet. The whole lecture assumes no taxes, no transaction costs, perfect markets.

MIGUEL: And the conclusion comes before the proof.

MEI: The professor states MM Proposition I up front, in a box: in a perfect capital market, the total value of a firm's securities is equal to the market value of the total cash flows generated by its assets, and is not affected by its choice of capital structure. Why: the assets produce the same cash flows however they're financed. Debt and equity only decide who receives them. The total to share stays the same.

MIGUEL: And the WACC with no taxes?

MEI: One slide. Set the tax rate to zero, the factor one minus the tax rate becomes one and disappears, and the WACC is the plain weighted average of the cost of equity and the cost of debt. That's the formula we work with today.

## A. Financing a project with equity only

MEI: Now the example that runs through the whole lecture, and I need to tell you the name of the firm. Tour moche SA.

MIGUEL: "Ugly Tower Incorporated." After the Tour Montparnasse renovation in the previous lecture.

MEI: Professor Saldarriaga clearly had fun with this one. An entrepreneur has a project: invest eight hundred today, and next year it pays fourteen hundred if the economy is strong or nine hundred if it's weak, each with probability one half. We're given the cost of equity: fifteen percent, the five percent risk-free rate plus a ten percent risk premium.

MIGUEL: Why "given"? Last lecture we spent an hour estimating it.

MEI: Because today the point isn't where the fifteen comes from, it's what happens to it when the financing changes. In practice it comes from the CAPM, exactly as in lecture six. Here the professor hands it to us so we can keep our eyes on the capital structure. Two states, two numbers, one rate. The whole lecture fits in a table with three rows.

MIGUEL: The question?

MEI: How much is the firm worth? With equity only, the cost of capital is just the cost of equity, fifteen percent. Step one: expected cash flow next year, half of fourteen hundred plus half of nine hundred, eleven hundred and fifty. Discount at fifteen percent: eleven fifty over one point one five, a thousand. The value of the firm is a thousand.

MIGUEL: And the entrepreneur?

MEI: She can sell the firm for a thousand, pay the eight hundred investment and keep two hundred. NPV: minus eight hundred plus a thousand, two hundred. Equity in a firm with no debt is called unlevered equity. And since we priced it at fifteen percent, the shareholders who buy it earn fifteen percent, by construction: forty percent in the strong state, minus ten in the weak one, average fifteen.

## B. The same project, financed another way

MEI: Same project. Now the entrepreneur borrows five hundred and sells equity for the rest. She can borrow at the risk-free rate, five percent, because even in a weak economy the project pays nine hundred, enough to repay. The loan is risk free. Next year the firm owes five hundred times one point zero five, five hundred and twenty-five, whatever the economy does.

MIGUEL: What's left for the shareholders?

MEI: Lenders are paid before shareholders. Strong economy: fourteen hundred minus five twenty-five, eight hundred and seventy-five. Weak economy: nine hundred minus five twenty-five, three hundred and seventy-five. Equity in a firm that also has debt is called levered equity.

MIGUEL: And the firm as a whole?

MEI: Put lenders and shareholders together. Strong: five twenty-five plus eight seventy-five, fourteen hundred. Weak: five twenty-five plus three seventy-five, nine hundred. Together they receive exactly the project's cash flows. The slide says it with five exclamation marks: these are the same values as for the unlevered firm. Nothing is created and nothing is lost.

MIGUEL: Five exclamation marks. He was excited.

MEI: He was, and rightly so, because this is the whole theorem in one line of a table. Now the Law of One Price: two investments that pay the same cash flows in every state of the economy must sell for the same price. The levered firm pays fourteen hundred or nine hundred, exactly like the unlevered one, so it's worth the same: a thousand.

MIGUEL: And the equity?

MEI: Debt plus equity equals a thousand, debt is five hundred, so equity is five hundred. Now the entrepreneur's table. Equity only: she sells shares for a thousand, borrows nothing, raises a thousand, invests eight hundred, keeps two hundred. Debt and equity: sells shares for five hundred, borrows five hundred, raises a thousand, invests eight hundred, keeps two hundred. Same two hundred. She's indifferent.

## The common fallacy

MEI: Now the slide I'd put on the exam. Before Modigliani and Miller, many people reasoned like this. Step one: what do shareholders expect next year? Eight seventy-five or three seventy-five, average six hundred and twenty-five. Step two: what is that worth today? Discount at fifteen percent, the rate we used for the firm without debt: six twenty-five over one point one five, five hundred and forty-three. Step three: so the equity is worth five forty-three, more than the five hundred from the Law of One Price. Borrowing creates value out of nothing.

MIGUEL: Which contradicts the Law of One Price. But hold on. The shareholders really do expect six twenty-five. That part isn't wrong.

MEI: That part is perfectly right. The expected cash flow is six twenty-five, no dispute. The error is one step later, and it's the most common error in all of corporate finance: using a discount rate that belongs to a different risk. Fifteen percent was the price of the unlevered risk. The levered shareholders don't bear the unlevered risk any more.

MIGUEL: So the numerator is fine and the denominator is wrong.

MEI: The numerator is fine and the denominator is wrong. Look at what the levered shareholders actually earn. They pay five hundred today. Strong economy: eight seventy-five, a return of plus seventy-five percent. Weak: three seventy-five, minus twenty-five percent. Expected return: half of seventy-five plus half of minus twenty-five, twenty-five percent. Not fifteen.

MIGUEL: Why twenty-five?

MEI: Because the economy is the same in both cases, but how much the shareholders' return moves with it changed. Without debt, the return goes from minus ten to plus forty: a swing of fifty points. With debt, from minus twenty-five to plus seventy-five: a swing of a hundred points. Levered equity is riskier, so investors require a higher expected return. Fifteen percent was the price of the first risk, twenty-five is the price of the second. Discount at the right rate and the puzzle disappears: six twenty-five over one point two five, five hundred.

MIGUEL: Cheap debt, dearer equity.

MEI: On its own, debt looks cheap: five percent against twenty-five for the levered equity. But the firm uses both. Weight each by its value: half times five percent plus half times twenty-five percent, fifteen percent. The same fifteen as with equity alone. The cheap debt is exactly offset by the dearer equity.

## Exercise: borrow only 200

MEI: Same project, same entrepreneur, but she borrows only two hundred at five percent. Step one, the equity value: debt plus equity is still a thousand, so equity is eight hundred. Step two, the cash flows: the firm owes two hundred times one point zero five, two hundred and ten. Shareholders get fourteen hundred minus two ten, eleven hundred and ninety, or nine hundred minus two ten, six hundred and ninety.

MIGUEL: Returns.

MEI: On eight hundred paid today: eleven ninety over eight hundred minus one, plus forty-eight point seven five percent. Six ninety over eight hundred minus one, minus thirteen point seven five percent. Expected: seventeen point five percent. Step four, the average cost of capital: zero point eight times seventeen point five plus zero point two times five. Fifteen percent. Again.

MIGUEL: So the cost of equity goes fifteen, seventeen and a half, twenty-five as the debt goes zero, two hundred, five hundred.

MEI: And the firm's average cost stays at fifteen all the way. Less debt than before, so the equity is less risky than with five hundred of debt, but riskier than with none. The summary slide of section B: lenders are paid first, shareholders get what remains. Debt and equity together receive the project's cash flows. By the Law of One Price they're worth what the project is worth, a thousand, whatever the mix. Shareholders of a levered firm earn a higher expected return because they bear more risk. And the average cost of capital does not move.

## C. Perfect markets and MM Proposition I

MEI: Section C makes it general. Our example made hidden assumptions, and Modigliani and Miller spell them out. Together they define a perfect capital market. Five conditions.

MIGUEL: One.

MEI: Investors and firms trade the same securities at fair prices, equal to the present value of their cash flows. Two: no taxes, transaction costs or issuance costs. Nothing leaked out when she sold the equity or took the loan. Three: no bankruptcy costs. Default itself destroys no cash flow; lenders simply receive what's left. Four: all investors can borrow and lend without restrictions at the risk-free rate. Our entrepreneur borrowed at the same five percent as anyone else. Five: financing does not change the project's cash flows, and does not reveal new information about them.

MIGUEL: And remove any one of them?

MEI: And the conclusion can change. That's the subject of the next lectures. But with all five, MM Proposition I: in a perfect capital market, the total value of a firm's securities equals the market value of the total cash flows generated by its assets, and is not affected by the choice of capital structure. In plain words: the pie is the same size however you slice it. The cash flows are the pie, debt and equity are the slices. In our example the pie was worth a thousand with no debt, with two hundred of debt, and with five hundred.

MIGUEL: Two ways to see it.

MEI: The Law of One Price, as we did. And Miller's own version, with Yogi Berra. The pizza delivery man asks whether he wants the pizza cut into four or eight slices. Yogi says: cut it in eight, I'm feeling hungry tonight.

MIGUEL: Cutting the pizza differently doesn't make more pizza.

MEI: That sentence is MM Proposition I. And then the slide every student should read twice, "MM and the real world." Students ask why MM matters if real markets aren't perfect. Galileo showed that without friction all bodies fall at the same speed. Drop a feather and a stone and it doesn't hold. Galileo wasn't wrong; air friction slows some objects more than others. MM is the same kind of result. In practice capital structure does affect value, and MM tells us any such effect must come from a friction: taxes, bankruptcy costs, information problems.

MIGUEL: So the theorem is a map of where to look.

MEI: That's exactly it. Lectures nine and ten are the frictions, one by one.

## D. Homemade leverage

MEI: Section D. Suppose investors would prefer a different capital structure from the one the firm chose. Homemade leverage is the mechanism by which an investor combines the company's shares with other assets to reach the leverage they want. One condition: investors can borrow at the same rate as the firm.

MIGUEL: Increase the leverage yourself.

MEI: The investor wants more leverage. He borrows five hundred and buys the shares of the unlevered Tour moche. The table: buy unlevered equity, minus a thousand today, plus fourteen hundred or nine hundred next year. Borrow five hundred, plus five hundred today, minus five twenty-five next year either way. Total: minus five hundred today, plus eight seventy-five or three seventy-five next year. That is exactly what levered equity pays, for a cost of five hundred. By the Law of One Price, levered equity must be worth five hundred.

MIGUEL: And undo the firm's leverage.

MEI: The firm has borrowed five hundred, but the investor would prefer unlevered equity. He buys both the debt and the levered equity. Debt: five hundred today, five twenty-five next year. Levered equity: five hundred today, eight seventy-five or three seventy-five. Total: a thousand today, fourteen hundred or nine hundred next year. Same cash flows as unlevered equity, for a thousand. The debt he owns neutralizes the firm's debt.

MIGUEL: So the firm's choice changes nothing for him.

MEI: Either way, the investor picks the leverage he wants, so he won't pay more for one structure than for the other. That's the box.

MIGUEL: One objection. I can't borrow at five percent. My bank would laugh.

MEI: And that's exactly condition four of the perfect market: everyone borrows and lends at the risk-free rate. If you can't, then the firm can do something for you that you can't do yourself, and you might pay a little extra for the levered shares. That's a friction, and that's where capital structure starts to matter. Keep that objection, it's a good one, and it's the kind of thing the next lectures take seriously.

MIGUEL: So every time I find a hole in the argument, I've found a chapter.

MEI: That's the way to read Modigliani and Miller.

## The proof of MM I

MEI: Three slides, and here's where we give you the shape and send you to the tables. Take two firms with the same assets, paying fourteen hundred or nine hundred next year. U has no debt. L has borrowed five hundred at five percent. The claim: U and L must sell for the same price. The method: suppose the prices were different. Using the two homemade-leverage tricks, an investor could pocket money today without changing what he receives next year. Free money. Everyone would rush for it, and prices would move until they're equal.

MIGUEL: Case one.

MEI: U is too expensive. Suppose U sells for a thousand and fifty while L's debt and shares sell for five hundred plus five hundred, a thousand. An investor who owns U sells it for a thousand and fifty, buys all of L's debt for five hundred and all of L's shares for five hundred. Next year, he gave up fourteen hundred or nine hundred, and he receives five twenty-five plus eight seventy-five, or five twenty-five plus three seventy-five: fourteen hundred or nine hundred. Nothing changes next year. Today he's fifty richer. Everyone does it, U's price falls, L's rises, until they're equal.

MIGUEL: Case two.

MEI: U is too cheap. Suppose U sells for nine hundred and ninety while L's shares sell for five hundred and ten, so L is worth a thousand and ten. An investor who owns L's shares sells them for five ten, borrows five hundred himself, and buys U for nine ninety. Today: plus five ten, plus five hundred, minus nine ninety, twenty in his pocket. Next year: minus eight seventy-five or three seventy-five from the shares he sold, minus five twenty-five on the loan, plus fourteen hundred or nine hundred from U. Zero either way. Twenty today for nothing. Everyone sells L and buys U until the prices meet.

MIGUEL: So both directions push to the same place.

MEI: Both directions, and the box closes it: by the Law of One Price, the value of U equals the value of L equals debt plus levered equity. Firm value does not depend on the debt. This is MM I. The two tables are on slides 41 and 42; go through each row once, it takes two minutes and then you own the proof.

## E. The market value balance sheet

MEI: Last section, one slide. According to MM I, the market value of the firm's assets equals the market value of the securities it issued. So equity equals assets minus debt and other liabilities. The table from the textbook: on the left, tangible assets, cash, plant and equipment, inventory; and intangible assets, intellectual property, reputation, human capital. On the right, debt, short-term, long-term, convertible; and equity, common stock, preferred stock, warrants. Both columns add up to the same total.

MIGUEL: How is it different from an accounting balance sheet?

MEI: Every asset counts, including the intangibles, and everything is at market value, which is often hard to estimate. It's the balance sheet an investor would draw, not the one the auditor signs.

MIGUEL: Human capital on a balance sheet. The auditor would faint.

MEI: The auditor would, and yet the market prices it every day. Think of a consulting firm or a software company: the plant and equipment are a few laptops, and the market value is billions. The difference is people, reputation, intellectual property. The accounting balance sheet doesn't see it. The market value balance sheet does, because it starts from the price investors actually pay for the securities and works backwards to what the assets must be worth.

MIGUEL: So equity is whatever is left once you take the debt out of that market value.

MEI: Equity equals assets minus debt and other liabilities, at market values. That identity is the tool we'll use in lecture eight to follow what a recapitalization does to a share price.

## What to remember

MEI: Four points. MM Proposition I: in a perfect capital market the total value of a firm's securities equals the value of its assets, whatever the capital structure. Perfect market means fair prices, no taxes or transaction or issuance costs, no bankruptcy costs, everyone borrows and lends at the risk-free rate, and financing changes neither the cash flows nor the information about them. Leverage makes equity riskier: debt has payment priority, shareholders demand more, the cost of equity rises. And homemade leverage: investors can borrow or lend to get the leverage they want, so the firm's choice gives them nothing extra.

MIGUEL: And the loose end?

MEI: The loose end is the number. We saw the cost of equity go from fifteen to seventeen and a half to twenty-five as debt went from zero to two hundred to five hundred. Today we found those numbers by hand, state by state. Lecture eight gives the formula that produces them directly from the debt-to-equity ratio: MM Proposition II. Same example, same Tour moche, one more equation.

## Wrap-up: the recap

MEI: Lecture seven in one minute. One project, eight hundred in, fourteen hundred or nine hundred out, cost of equity fifteen percent. With equity only, the firm is worth a thousand and the entrepreneur keeps two hundred. With five hundred of risk-free debt at five percent, lenders get five twenty-five, shareholders get eight seventy-five or three seventy-five, and together that's still fourteen hundred or nine hundred, so the firm is still worth a thousand and the equity five hundred. The entrepreneur keeps the same two hundred.

MIGUEL: The fallacy.

MEI: Discounting the levered equity's expected six twenty-five at fifteen percent gives five forty-three. Wrong rate. Levered equity swings a hundred points instead of fifty, so it requires twenty-five percent, and six twenty-five over one point two five is five hundred. Cheap debt at five and dear equity at twenty-five average out to the same fifteen. With two hundred of debt: equity eight hundred, return seventeen point five, average still fifteen.

MIGUEL: The theorem.

MEI: Five conditions make a perfect market. MM Proposition I: the pie is the same size however you slice it. Homemade leverage lets any investor add or undo leverage, so a price gap between a levered and an unlevered firm is free money, and free money doesn't last. And the market value balance sheet: all assets at market value, equal to all securities at market value.

MIGUEL: The quiz.

MEI: Why five hundred and not five forty-three: five forty-three uses the unlevered rate on levered cash flows; at the right rate, twenty-five percent, six twenty-five discounts to five hundred, which also equals a thousand minus five hundred. The five conditions: fair prices; no taxes, transaction or issuance costs; no bankruptcy costs; unrestricted borrowing and lending at the risk-free rate; financing changes neither cash flows nor information. And borrow seven hundred and fifty: equity is worth two hundred and fifty. The firm owes seven eighty-seven point five, so equity gets six twelve point five or one twelve point five, returns plus one hundred and forty-five percent or minus fifty-five, expected forty-five percent. A forty percent risk premium, four times the unlevered premium, for four times the sensitivity.

MIGUEL: My takeaway: in a perfect world, how you slice the pizza changes who eats what, never how much pizza there is. And if you ever find the levered Tour moche selling for five forty-three, call me before you call the professor.

MEI: Read chapters 14.1 and 14.2, redo the seven hundred and fifty case on your own, and walk through the two arbitrage tables once with a pencil. Thanks for listening to The Finance and Economics Papers Podcast.

MIGUEL: See you in the next lecture.
