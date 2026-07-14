from manim import * 
from manim.mobject.svg.svg_mobject import SVGMobject
from manim_slides import Slide

screen_width = 16/9 * 8

config.background_color = "#fcfbf1"
black_color = "#323030"
blue_color = "#6883FB"
red_color = "#F1534D"
green_color = "#5CB85C"
yellow_color = "#ff6f1b"
head_color = "#fcad63"
highlight_color = "#fff691"

Text.set_default(color = black_color)
Tex.set_default(color = black_color)
MathTex.set_default(color = black_color)
Dot.set_default(color = black_color)

def step_graph(x_size, y_size):
    x_min, x_max = -0.2, 1.5
    y_min, y_max = -0.2, 1.5
    tau = 0.5
    T = 1

    axes = Axes(
        x_range=[x_min, x_max, 0.5],
        y_range=[y_min, y_max, 1],
        x_length=x_size,
        y_length=y_size,
        axis_config={"color": black_color}
    )

    # Etiquetas de ejes
    x_label = MathTex(r"t").next_to(axes.x_axis.get_right(), DOWN)
    y_label = MathTex(r"f(t)").next_to(axes.y_axis.get_top(), LEFT)

    # Construir la función escalón con segmentos para evitar muestreo borroso
    left_segment = Line(
        axes.coords_to_point(0, 0),
        axes.coords_to_point(tau, 0),
        color=blue_color,
        stroke_width=4
    )
    right_segment = Line(
        axes.coords_to_point(tau, 1),
        axes.coords_to_point(T, 1),
        color=blue_color,
        stroke_width=4
    )
    # Salto en tau (línea corta para indicar discontinuidad)
    jump = DashedLine(
        axes.coords_to_point(tau, 0),
        axes.coords_to_point(tau, y_max),
        color=black_color,
        dash_length=0.08
    )

    # Línea vertical en tiempo T (destacada)
    vline = DashedLine(
        axes.coords_to_point(T, 0),
        axes.coords_to_point(T, y_max),
        color=red_color,
        dash_length=0.08,
        stroke_width=3.5
    )

    # Ticks y etiquetas abstractas para tau y T
    
    tau_label = MathTex(r"\tau").next_to(axes.coords_to_point(tau, 0), DOWN * 0.7)
    T_label = MathTex(r"T").next_to(axes.coords_to_point(T, 0), DOWN * 0.6)

    # Etiqueta de los niveles 0 y 1
    zero_label = MathTex(r"0").next_to(axes.coords_to_point(x_min, 0), LEFT * 0.25)
    one_label = MathTex(r"1").next_to(axes.coords_to_point(x_min, 1), LEFT * 0.25)

    group = VGroup(
        axes, x_label, y_label,
        left_segment, right_segment, jump,
        vline, tau_label, T_label,
        zero_label, one_label
    ).scale(0.9)

    return group

def delta_graph(x_size, y_size):

    x_min, x_max = -0.2, 1.5
    y_min, y_max = -0.2, 1.5
    tau = 0.5
    T = 1

    axes = Axes(
        x_range=[x_min, x_max, 0.5],
        y_range=[y_min, y_max, 1],
        x_length=x_size,
        y_length=y_size,
        axis_config={"color": black_color}
    )

    # Etiquetas de ejes
    x_label = MathTex(r"t").next_to(axes.x_axis.get_right(), DOWN)
    y_label = MathTex(r"f(t)").next_to(axes.y_axis.get_top(), LEFT)

    # Salto en tau (línea corta para indicar discontinuidad)
    jump = Arrow(
        axes.coords_to_point(tau, 0),
        axes.coords_to_point(tau, y_max),
        color=red_color,
        buff = 0.0
    )

    # Línea vertical en tiempo T (destacada)
    vline = DashedLine(
        axes.coords_to_point(T, 0),
        axes.coords_to_point(T, y_max),
        color=black_color,
        dash_length=0.08,
        stroke_width=3.5
    )

    # Ticks y etiquetas abstractas para tau y T
    
    tau_label = MathTex(r"\tau").next_to(axes.coords_to_point(tau, 0), DOWN * 0.7)
    T_label = MathTex(r"T").next_to(axes.coords_to_point(T, 0), DOWN * 0.6)

    # Etiqueta de los niveles 0 y 1
    zero_label = MathTex(r"0").next_to(axes.coords_to_point(x_min, 0), LEFT * 0.25)
    one_label = MathTex(r"1").next_to(axes.coords_to_point(x_min, 1), LEFT * 0.25)

    group = VGroup(
        axes, x_label, y_label, jump,
        vline, tau_label, T_label,
        zero_label, one_label
    ).scale(0.9)

    return group
        

class Bienal(Slide):

    def fadeout_all(self, **kwargs):
        """Fade out all the currents objects from screen"""

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )

    def remove_all(self, **kwargs):
        """Remove all the currents objects from screen"""

        self.remove(*self.mobjects)

    

    def construct(self):

        texTemplate = TexTemplate()
        texTemplate.add_to_preamble(r"\usepackage{physics, amsmath, amssymb}")
        
        self.wait(0.1)
        self.next_slide()
        self.remove_all()

        # -----------------------------------------------
        #                  TITLE SCREEN
        # -----------------------------------------------
        
        # banner = Text("XL Bienal de la RSEF").scale(1.1).to_edge(UP, buff = 0.5)
        banner = ImageMobject("./assets/banner_bienal.jpg").scale_to_fit_width(screen_width).to_edge(UP, buff = 0)
        title = VGroup(
            Text(r"Does The Stroboscopic Lindbladian Exist?"),
            Text(r"An Analytical Approach")
        ).arrange(DOWN, buff = 0.3)
        authors = VGroup(
            Text(r"Antonio de la M. Sojo López").scale(0.7),
            Text(r"Jesús Casado Pascual").scale(0.7)
        ).arrange(DOWN, buff = 0.15)

        # Logos 'n' stuff
        logo_us = ImageMobject("./assets/logos/logo_us.png").scale_to_fit_height(1)
        banner_min = ImageMobject("./assets/logos/min_banner.jpg").scale_to_fit_height(1)
        banners = Group(
            Group(
                logo_us,
                Text("PIF VII Plan Propio").scale_to_fit_width(logo_us.width)\
                    .next_to(logo_us, DOWN, buff=0.1)
            ),
            Group(
                banner_min,
                Text("PID2022-136228NB-C22").scale_to_fit_width(banner_min.width)\
                    .next_to(banner_min, DOWN, buff=0.1)
            )
        ).arrange(RIGHT, buff = 0.5).scale_to_fit_height(1.5)

        title_screen = VGroup(
            title,
            authors,
        ).scale_to_fit_width(0.6*screen_width).arrange(DOWN, buff=0.35)
        authors.shift(0.15*DOWN)
        banners.to_edge(DOWN, buff = 0.5)

        self.play(
            Write(title)
        )
        self.play(
            FadeIn(banner, shift = DOWN),
            Write(authors),
            FadeIn(banners, shift = UP)
        )

        # -----------------------------------------------
        #                 Floquet Theory
        # -----------------------------------------------

        self.next_slide()
        self.remove_all()

        title_floquet = Title("Motivation", include_underline=False)

        ev_eq_u = MathTex(r"\dv{}{t}\ket{\Psi(t)} = -\frac{i}{\hbar}H(t)\ket{\Psi(t)}", tex_template=texTemplate)
        ev_eq_L = MathTex(r"\dv{}{t}\rho(t) = \mathcal{L}(t)\rho(t)", tex_template=texTemplate)
        prop_U = MathTex(r"\ket{\Psi(t)} = U(t,t_0)\ket{\Psi(t_0)} \text{ (Unitary)}", tex_template=texTemplate)
        prop_L = MathTex(r"\rho(t_0)=\mathcal{E}(t,t_0)\rho(t_0) \text{ (CPTP Map)}", tex_template=texTemplate)
        periodic_row = [Tex(r"If $H(t+T) = H(t)$"), Tex(r"If $\mathcal{L}(t+T) = \mathcal{L}(t)$")]
        stroboscopic = [
                    MathTex(r"U(nT, 0) = ", r"e^{-\frac{i}{\hbar}nT H_\text{eff}}"),
                    MathTex(r"\mathcal{E}(nT, 0) = ", r"e^{nT \mathcal{G}_\text{eff}}")
        ]


        floquet_table = MobjectTable(
            [
                [MathTex(r"\ket{\Psi}\in\mathcal{H}", tex_template=texTemplate), MathTex(r"\rho\in L(\mathcal{H})", tex_template=texTemplate)],
                [
                    VGroup(
                        ev_eq_u,
                        prop_U
                    ).arrange(DOWN, buff = 0.5)
                ,
                    VGroup(
                        ev_eq_L,
                        prop_L
                    ).arrange(DOWN, buff = 0.5)
                ],
                periodic_row,
                stroboscopic
            ],
            col_labels=[Text("Closed"), Text("Open Lindbladian")],
            row_labels=[Text("State"), Text("Evolution"), Text("HOLA").set_opacity(0.0), Text("Floquet")],
            line_config = {"color": black_color}
        ).scale_to_fit_width(screen_width).shift(0.5*DOWN)
        #floquet_table.remove(*floquet_table.get_horizontal_lines())

        footnotes = Tex(r"CPTP $\equiv$ Completely Positive Trace Preserving Map")\
        .scale(0.7).next_to(floquet_table, DOWN, buff = 0.35)

        slide = VGroup(
            title_floquet,
            floquet_table,
            footnotes
        ).scale_to_fit_height(7.5).center()
        
        self.play(
            Write(title_floquet),
            Write(floquet_table.get_col_labels()),
            Write(floquet_table.get_row_labels()),
            Create(floquet_table.get_vertical_lines()),
            Create(floquet_table.get_horizontal_lines()),
            Write(footnotes)
        )
        
        for obj in floquet_table.get_columns()[1][1:]:
            self.next_slide()
            self.play(Write(obj))

        self.next_slide()
        
        connection_U = VGroup(
            Brace(ev_eq_u, color = red_color),
            SurroundingRectangle(stroboscopic[0][-1], color = red_color)
        )
        connection_U.add(
            Arrow(connection_U[0].get_bottom(), connection_U[-1].get_top(), buff = 0, color = red_color)
        )
        connection_U.add(
            Text("Floquet Engineering").scale(0.45).set_color(red_color)\
                .next_to(connection_U[-1], LEFT, buff = 0).shift(0.15*DOWN+0.1*RIGHT)
        )

        self.remove(periodic_row[0])
        self.play(Create(connection_U))

        self.wait(0.3)

        self.next_slide()
        self.add(periodic_row[0])
        self.remove(connection_U)
        self.play(Write(floquet_table.get_columns()[2][1]))

        for obj in floquet_table.get_columns()[2][2:-1]:
            self.next_slide()
            self.play(Write(obj))

        self.next_slide()
        self.add(floquet_table.add_highlighted_cell((5,3), color = highlight_color))
        self.play(
            Write(floquet_table.get_columns()[2][-1]))

        self.next_slide()
        
        connection_L = VGroup(
            Brace(ev_eq_L, color = red_color),
            SurroundingRectangle(stroboscopic[1][-1], color = red_color)
        )
        connection_L.add(
            Arrow(connection_L[0].get_bottom(), connection_L[-1].get_top(), buff = 0, color = red_color)
        )
        connection_L.add(
            Text("Floquet Engineering?").scale(0.4).set_color(red_color)\
                .next_to(connection_L[-1], LEFT, buff = 0).shift(0.15*DOWN+0.1*RIGHT)
        )

        self.remove(periodic_row[1])
        self.play(Create(connection_L))

        self.wait(0.3)

        self.next_slide()
        self.add(periodic_row[1])
        self.remove(connection_L)

        self.play(
            Transform(
                floquet_table.get_rows()[-1][1],
                Tex(r"$H_\text{eff}$ is a Hamiltonian").scale(1).set_color(green_color).move_to(floquet_table.get_rows()[-1][1])
            )
        )

        self.next_slide()
        self.play(
            Transform(
                floquet_table.get_rows()[-1][2],
                Tex(r"$\mathcal{G}_\text{eff}$ is ???").scale(1.5).set_color(red_color).move_to(floquet_table.get_rows()[-1][2])
            )
        )

        # -----------------------------------------------
        #        Problem Statement and current solution
        # -----------------------------------------------

        self.next_slide()
        self.remove_all()

        title_problem = Title(r'Is the Floquet Generator $\mathcal{G}$ a Lindbladian?')
        title_problem.underline.color = black_color

        cptp_rect = Rectangle(height = 5.5, width = 9, color = blue_color, fill_color = blue_color, fill_opacity=0.1)
        cptp_title = Tex(r"$\mathcal{E}$ is CPTP", color = blue_color).scale_to_fit_height(0.35).move_to(cptp_rect.get_top() + 0.35*DOWN)
        cptp_rect.set_z_index(1)
        cptp_title.set_z_index(1)
        cptp_set = VGroup(
            cptp_title,
            cptp_rect
        )

        linbladian_rect = Rectangle(height = 4.25, width = 0.6*11, color = yellow_color, fill_color = yellow_color, fill_opacity=0.1)\
            .shift(cptp_rect.width/8*RIGHT+0.5*DOWN)
        linbladian_title = Tex(r"$\mathcal{G}$ is Lindbladian", color = yellow_color).scale_to_fit_height(0.35).move_to(linbladian_rect.get_top() + 0.35*DOWN)
        linbladian_rect.set_z_index(2)
        linbladian_title.set_z_index(2)
        linbladian_set = VGroup(
            linbladian_title,
            linbladian_rect
        )

        TD_rect = Rectangle(height = 3, width = 0.25*11, color = green_color, fill_color = green_color, fill_opacity=0.1)\
            .shift(cptp_rect.width/8*RIGHT-linbladian_rect.width/4*RIGHT+1*DOWN)
        TD_title = VGroup(
            Tex(r"Non-Constant Gen.", color = green_color).scale(0.8),
            MathTex(r"\mathcal{E}=\mathcal{T}e^{\int d\tau\mathcal{G}(\tau)}", color = green_color).scale(0.9)
        ).arrange(DOWN, buff = 0.2).scale_to_fit_height(0.8).scale_to_fit_height(0.8).move_to(TD_rect.get_top() + 0.55*DOWN)
        TD_rect.set_z_index(3)
        TD_title.set_z_index(3)
        TD_set = VGroup(
            TD_title,
            TD_rect
        )

        ITD_rect = Rectangle(height = 3, width = 0.25*11, color = green_color, fill_color = green_color, fill_opacity=0.1)\
            .shift(cptp_rect.width/8*RIGHT+linbladian_rect.width/4*RIGHT+1*DOWN)
        ITD_title = VGroup(
            Tex(r"Constant Gen.", color = green_color),
            MathTex(r"\mathcal{E}=e^{t\mathcal{L}}", color = green_color)
        ).arrange(DOWN, buff = 0.2).scale_to_fit_height(0.8).move_to(ITD_rect.get_top() + 0.55*DOWN)
        ITD_rect.set_z_index(3)
        ITD_title.set_z_index(3)
        ITD_set = VGroup(
            ITD_title,
            ITD_rect
        )

        uni_rect = Rectangle(height = 1.5, width = 2, color = red_color, fill_color = red_color, fill_opacity=0.1)\
            .move_to(ITD_rect).shift(0.5*DOWN)
        uni_title = Tex(r"Unitary", color = red_color).scale_to_fit_height(0.35).move_to(uni_rect)
        uni_rect.set_z_index(4)
        uni_title.set_z_index(4)
        uni_set = VGroup(
            uni_title,
            uni_rect
        )

        sets = VGroup(cptp_set, linbladian_set, TD_set, ITD_set, uni_set).shift(0.5*DOWN)
        
        self.play(Write(title_problem), FadeIn(cptp_set))
        self.wait(0.3)
        self.next_slide()
        self.play(FadeIn(linbladian_set))
        self.wait(0.3)
        self.next_slide()
        self.play(FadeIn(TD_set),FadeIn(ITD_set)) 
        #self.play(FadeIn(ITD_set))
        self.wait(0.3)
        self.next_slide()
        self.play(FadeIn(uni_set))
        self.wait(0.3)

        self.next_slide()

        # -----------------------------------------------
        #      Wolf, Rivas and Hall results
        # -----------------------------------------------

        self.play(FadeOut(sets))

        lindbladian = MathTex(r"\mathcal{L}[\rho]", 
                              r"=", 
                              r"-\frac{i}{\hbar}[H,\rho]", 
                              r"+",
                              r"\sum_{k=1}^{d^2-1}",r"K_{\alpha,\beta}",
                              r"\left(L_\alpha\rho L_\beta(t)^\dagger - \frac{1}{2}\{L_\beta^\dagger L_\alpha, \rho\} \right)", tex_template=texTemplate).scale(0.8)
        lindbladian.next_to(title_problem, DOWN, buff = 0.5)

        surrect1 = SurroundingRectangle(lindbladian[2], color = red_color, buff = 0.1)
        surrect2 = SurroundingRectangle(lindbladian[4:], color = blue_color, buff = 0.1)

        text1 = Tex(r"A linear map $\mathcal{G}: L(\mathcal{H}) \rightarrow L(\mathcal{H})$ is Lindbladian iff:").next_to(lindbladian, DOWN, buff = 0.5)
        conditions = VGroup(
            Tex(r"$\mathcal{G}$ is Hermiticity preserving"), MathTex(r"\Longleftrightarrow"), MathTex(r"\mathcal{G}[X^\dagger] = (\mathcal{G}[X])^\dagger"),
            Tex(r"$\mathcal{G}$ generates trace preserving maps"), MathTex(r"\Longleftrightarrow"), MathTex(r"\mathcal{G}^*[I] = 0"),
            Tex(r"$\mathcal{G}$ is Conditionally Completely Positive"), MathTex(r"\Longleftrightarrow"), MathTex(r"K \ge 0")
        ).arrange_in_grid(3,3, buff = 0.35).next_to(text1, DOWN, buff = 0.5).scale(0.8)

        refs1 = VGroup(
            Tex(r"\textbf{[Wolf08]}: M. M. Wolf et al., Phys. Rev. Lett. 101, 150402 (2008)"),
            Tex(r"\textbf{[Hall14]}: M. J. W. Hall et al., Phys. Rev. A 89, 042120 (2014)")
        ).arrange(DOWN, aligned_edge = LEFT, buff = 0.2).to_edge(DOWN, buff = 0.15).scale(0.4)

        self.play(Write(lindbladian))

        self.next_slide()
        self.play(Create(surrect1))
        self.next_slide()
        self.play(FadeOut(surrect1), Create(surrect2))

        self.next_slide()
        self.play(FadeOut(surrect2), Write(text1), Write(refs1))
        self.next_slide()
        self.play(Write(conditions[0:3]))
        self.next_slide()
        self.play(Write(conditions[3:6]))
        self.next_slide()
        self.play(Write(conditions[6:]))
        self.next_slide()
        self.play(
            lindbladian[5].animate.set_color(red_color),
            conditions[-1][-1].animate.set_color(red_color)
        )
        Ko = lindbladian[5].copy()
        self.play(Succession(Ko.animate.move_to(conditions[-1][-1]), FadeOut(Ko)))

        self.next_slide()
        self.fadeout_all()
        # -----------------------------------------------
        #              Measures of Markovianity
        # -----------------------------------------------

        title_problem = Title(r'Measures of Lindbladianity?')
        title_problem.underline.color = black_color

        text1 = Tex(r"If $\mathcal{G}$ is HP and TP, we can define its Lindbladianity").next_to(title_problem, DOWN, buff = 0.25).scale(0.8)

        mathtable = [
            [MathTex(r"\mu_W = \text{min}\{\mu\,|\,\mu I+\Omega_{\perp} C_\mathcal{G} \Omega_{\perp} \ge_0\}"), MathTex(r"\mu_R = \lim_{\epsilon\rightarrow 0^+} \frac{||(1+\epsilon \mathcal{G}\otimes I)[\Omega]||_1 - 1}{\epsilon}")],
            [MathTex(r"\mu_W = \frac{1}{d}|\text{max}\{0, -\gamma_1, \dots, -\gamma_{d^2}\}|"), MathTex(r"\mu_R = \frac{1}{d}\sum_{j = 1}^{d^2}(|\gamma_j|-\gamma_j)")],
            [Tex(r"Adding isotropic noise"), Tex(r"Markovian divisility")]
        ]
        lindbladianity = MobjectTable(
            mathtable,
            col_labels=[Text("Wolf"), Text("Rivas")],
            row_labels=[Text("Definition"), Text("Measure"), Text("Motivation")],
            line_config={"color": black_color}
        ).scale_to_fit_width(0.85*screen_width).next_to(text1, DOWN, buff = 0.5)

        text2 = MathTex(r"\text{Eigenvalues }\rho(K) = \{\gamma_1, \dots, \gamma_{d^2}\}").scale(0.7).to_corner(DOWN+LEFT, buff = 0.5)

        refs2 = VGroup(
            Tex(r"\textbf{[Wolf08]}: M. M. Wolf et al., Phys. Rev. Lett. 101, 150402 (2008)"),
            Tex(r"\textbf{[Rivas10]}: A. Rivas et al., Phys. Rev. Lett. 105, 050403 (2014)"),
            Tex(r"\textbf{[Hall14]}: M. J. W. Hall et al., Phys. Rev. A 89, 042120 (2014)")
        ).arrange(DOWN, aligned_edge = LEFT, buff = 0.2).scale(0.4).to_corner(DOWN+RIGHT, buff = 0.5)

        self.play(Write(title_problem), Write(text1), Write(text2), Write(refs2))
        self.next_slide()
        self.play(
            Write(lindbladianity.get_horizontal_lines()),
            Write(lindbladianity.get_vertical_lines()),
            Write(lindbladianity.get_col_labels()),
            Write(lindbladianity.get_row_labels()),
            Write(lindbladianity.get_entries_without_labels())
        )

        # -----------------------------------------------
        #                   Schnell
        # -----------------------------------------------

        self.next_slide()
        self.fadeout_all()

        title_problem = Title(r'Current published studies')
        title_problem.underline.color = black_color

        text1 = VGroup(
            Tex(r"Numerical study of a driven two-level system with dissipation").scale(0.8),
            Tex(r"Always HP and TP, but not always CCP").scale(0.8),
        ).arrange(DOWN, buff = 0.2).next_to(title_problem, DOWN, buff = 0.5)
        schnell_fig = ImageMobject("./assets/schnell.png").scale_to_fit_height(3.5)
        h_S = MathTex(r"H(t) =\frac{\Delta}{2}\sigma_z+E \cos{(\omega t - \phi)}\sigma_x").scale(0.8)
        l_S = MathTex(r"L = \sqrt{\gamma}\sigma_-").scale(0.8)

        schnell_group = Group(
            schnell_fig,
            VGroup(
                h_S,
                l_S
            ).arrange(DOWN, buff = 0.5)
        ).arrange(RIGHT, buff = 1).next_to(text1, DOWN, buff = 0.5)


        refs3 = VGroup(
            Tex(r"\textbf{[Schnell20]}: A. Schnell et al., Phys. Rev. B 101, 100301(R) (2020)")
        ).arrange(DOWN, aligned_edge = LEFT, buff = 0.2).scale(0.4).to_corner(DOWN+RIGHT, buff = 0.5)

        self.play(Write(title_problem), Write(text1), Write(refs3))
        self.next_slide()
        self.play(FadeIn(schnell_fig, shift = DOWN), Write(schnell_group[1]))

        # -----------------------------------------------
        #                   BIT FLIP
        # -----------------------------------------------

        self.next_slide()
        self.remove_all()

        title_problem = Title(r'Our approach: Analytical study of simple systems')
        title_problem.underline.color = black_color

        text1 = MathTex(r"H(t) = f(t)E\sigma_z\qquad L = \sqrt{\gamma}\sigma_x").scale(0.8).next_to(title_problem, DOWN, buff = 0.5)

        stepg = step_graph(4, 3)
        axes, x_label, y_label, \
        left_segment, right_segment, jump, \
        vline, tau_label, T_label, \
        zero_label, one_label = stepg

        regions1img = ImageMobject("./assets/fig1.png").scale_to_fit_height(4)
        regions1 = Group(
                regions1img,
                MathTex(r"\gamma = 1, \tau = T/2").scale(0.6)
        ).arrange(DOWN, buff = 0.1).center()

        figs1 = Group(
            stepg,
            regions1
        ).arrange(RIGHT, buff = 1).next_to(text1, DOWN, buff = 0.35)

        figs1[0].shift(0.5*(RIGHT+UP))
        figs1[1][1].shift(0.7*LEFT)

        text2 = Tex(r"Spin with an external field and random bit-flip errors").scale(0.8).next_to(figs1, DOWN, buff = 0.5)
        text3 = Tex(r"Always TP, but not HP nor CPP").scale(0.8).next_to(figs1, DOWN, buff = 0.5)
        
        self.play(Write(title_problem))

        self.play(Write(text1))
        self.next_slide()
        self.play(Create(axes), Write(x_label), Write(y_label), time = 0.2)
        self.play(Create(left_segment), Create(right_segment), time = 0.2)
        self.play(Create(jump), Create(vline), time = 0.2)
        self.play(Write(tau_label), Write(T_label), Write(zero_label), Write(one_label), time = 0.2)
        self.play(FadeIn(regions1, shift = UP))
        self.play(Write(text2))

        self.next_slide()
        self.play(ReplacementTransform(text2, text3))

        
        # -----------------------------------------------
        #                 DELTA LIMIT
        # -----------------------------------------------

        self.next_slide()
        self.play(FadeOut(figs1), FadeOut(text3))

        title_problem = Title(r'Our approach: Analytical study of simple systems')
        title_problem.underline.color = black_color

        text11 = MathTex(r"\Delta t H(t) = f(t)\alpha \sigma_z\qquad L = \sqrt{\gamma}\sigma_x").scale(0.8).next_to(title_problem, DOWN, buff = 0.5)

        stepg = delta_graph(4, 3)
        axes, x_label, y_label, jump, \
        vline, tau_label, T_label, \
        zero_label, one_label = stepg

        regions1img = ImageMobject("./assets/fig1Delta.png").scale_to_fit_height(4)
        regions1 = Group(
                regions1img,
                MathTex(r"\gamma = 1, \tau = T").scale(0.6)
        ).arrange(DOWN, buff = 0.1).center()

        figs1 = Group(
            stepg,
            regions1
        ).arrange(RIGHT, buff = 1).next_to(text1, DOWN, buff = 0.35)

        figs1[0].shift(0.5*(RIGHT+UP))
        figs1[1][1].shift(0.7*LEFT)

        text2 = Tex(r"Spin with random bit-flip errors that is `kicked'").scale(0.8).next_to(figs1, DOWN, buff = 0.5)
        text3 = Tex(r"Only Lindbladian in zero measure curves").scale(0.8).next_to(figs1, DOWN, buff = 0.5)

        self.play(ReplacementTransform(text1, text11))
        self.next_slide()
        self.play(Create(axes), Write(x_label), Write(y_label), time = 0.2)
        self.play(Create(jump), Create(vline), time = 0.2)
        self.play(Write(tau_label), Write(T_label), Write(zero_label), Write(one_label), time = 0.2)
        self.play(FadeIn(regions1, shift = UP))
        self.play(Write(text2))
        self.next_slide()
        self.play(ReplacementTransform(text2, text3))

        self.wait(0.3)

        # -----------------------------------------------
        #                 DELTA LIMIT 2
        # -----------------------------------------------

        self.next_slide()
        self.play(FadeOut(figs1), FadeOut(text3))

        figs = Group(
            Group(
                ImageMobject("./assets/fig1Delta2.png").scale_to_fit_height(4),
                MathTex(r"\gamma = 1, \tau = T").scale(0.6)
            ).arrange(DOWN, buff = 0.1),
            Group(
                ImageMobject("./assets/fig3Delta.png").scale_to_fit_height(4),
                MathTex(r"\gamma = 1, \tau = 0.92T").scale(0.6)
            ).arrange(DOWN, buff = 0.1),
            Group(
                ImageMobject("./assets/fig2Delta.png").scale_to_fit_height(4),
                MathTex(r"\gamma = 1, \tau = 0.5T").scale(0.6)
            ).arrange(DOWN, buff = 0.1)
        ).arrange(RIGHT, buff = 0.15).shift(DOWN)
        
        figs[0][1].shift(0.3*RIGHT)
        figs[1][1].shift(0.3*RIGHT)
        figs[2][1].shift(0.7*LEFT)

        self.play(FadeIn(figs, shift = UP))

        # -----------------------------------------------
        #                Conclusions
        # -----------------------------------------------

        self.next_slide()
        self.remove_all()

        title_problem = Title(r'Conclusions')
        title_problem.underline.color = black_color

        conclusions = VGroup(
            Tex(r"1. Analytical study of simple systems is possible"),
            Tex(r"2. The Hermiticity preserving property is not alwayws garanteed"),
            Tex(r"3. Zero measure curves of Lindbladianity. Can't be found numerically"),
            Tex(r"4. Defined Lindbladianity measures are only useful for HP and TP cases")
        ).scale_to_fit_width(0.85*screen_width).arrange(DOWN, aligned_edge = LEFT, buff = 0.5)

        self.play(Write(title_problem))

        self.next_slide()
        self.play(Write(conclusions[0]))
        self.next_slide()
        self.play(Write(conclusions[1]))
        self.next_slide()
        self.play(Write(conclusions[2]))
        self.next_slide()
        self.play(Write(conclusions[3]))


        # -----------------------------------------------
        #                   Bye Bye
        # -----------------------------------------------

        self.next_slide()
        self.remove_all()

        end_slide = VGroup(
            Tex(r"Thank you for your attention! \\ Any questions?").scale(1.25),
            SVGMobject("./assets/qr.svg").scale_to_fit_height(2.5)
        ).arrange(DOWN, buff = 0.5).center()

        self.play(Write(end_slide[0]), FadeIn(end_slide[1], shift = UP))
        self.wait(0.1)
