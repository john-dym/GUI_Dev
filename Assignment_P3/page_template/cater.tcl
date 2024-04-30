#############################################################################
# Generated by PAGE version 8.0
#  in conjunction with Tcl version 8.6
#  Mar 30, 2024 06:33:38 PM EDT  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    ::vTcl::MessageBox -title Error -message  "You must open project files from within PAGE."
    exit}


set vTcl(actual_gui_font_dft_desc)  TkDefaultFont
set vTcl(actual_gui_font_dft_name)  TkDefaultFont
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
########################################### 
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) gray40
set vTcl(analog_color_p) #c3c3c3
set vTcl(analog_color_m) beige
set vTcl(tabfg1) black
set vTcl(tabfg2) white
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
########################################### 
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
set vTcl(project_theme) default



proc vTclWindow.top1 {base} {
    global vTcl
    if {$base == ""} {
        set base .top1
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    set target $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background #f5deb5 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 
    wm focusmodel $top passive
    wm geometry $top 600x450+1033+291
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 2740 1055
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    set toptitle "Catering"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "frmCatering" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    button "$top.but47" \
        -activebackground #d9d9d9 -activeforeground black -background #f5deb5 \
        -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 11 -weight bold" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -relief groove \
        -text "Calculate" 
    vTcl:DefineAlias "$top.but47" "btnCalculate" vTcl:WidgetProc "frmCatering" 1
    button "$top.but48" \
        -activebackground #d9d9d9 -activeforeground black -background #f5deb5 \
        -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 11 -weight bold" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -relief groove \
        -text "Clear" 
    vTcl:DefineAlias "$top.but48" "btnClear" vTcl:WidgetProc "frmCatering" 1
    entry "$top.ent48" \
        -background white -disabledforeground #a3a3a3 \
        -font "-family {Courier New} -size 12" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 \
        -insertbackground #000000 -justify center -selectbackground #d9d9d9 \
        -selectforeground black -textvariable "fldPoints" -width 54 
    vTcl:DefineAlias "$top.ent48" "EntryLoyaltyPoints" vTcl:WidgetProc "frmCatering" 1
    label "$top.lab48" \
        -activebackground #f5deb5 -activeforeground black -anchor w \
        -background #f5deb5 -compound left -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 12 -weight bold" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 \
        -text "Loyalty Points" 
    vTcl:DefineAlias "$top.lab48" "Label2" vTcl:WidgetProc "frmCatering" 1
    label "$top.lab50" \
        -activebackground #f5deb5 -activeforeground black -background #f5deb5 \
        -compound center -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 18 -weight bold" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -text "Catering" 
    vTcl:DefineAlias "$top.lab50" "lblTitle" vTcl:WidgetProc "frmCatering" 1
    label "$top.lab51" \
        -activebackground #f5deb5 -activeforeground black -background #f5deb5 \
        -compound center -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 13 -weight bold" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 \
        -text "Star Market" 
    vTcl:DefineAlias "$top.lab51" "lblStore" vTcl:WidgetProc "frmCatering" 1
    label "$top.lab47" \
        -activebackground #d9d9d9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 9" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -text "Label" 
    vTcl:DefineAlias "$top.lab47" "lblPicture" vTcl:WidgetProc "frmCatering" 1
    frame "$top.fra48" \
        -borderwidth 2 -background #fdf7e7 -height 165 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -width 285 
    vTcl:DefineAlias "$top.fra48" "FrameFoodChoice" vTcl:WidgetProc "frmCatering" 1
    set site_3_0 $top.fra48
    radiobutton "$site_3_0.rad47" \
        -activebackground #d9d9d9 -activeforeground black -anchor w \
        -background #fdf7e7 -compound left -disabledforeground #a3a3a3 \
        -font "-family {Courier New} -size 10" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -justify left \
        -text "Radio" 
    vTcl:DefineAlias "$site_3_0.rad47" "radioFood01" vTcl:WidgetProc "frmCatering" 1
    radiobutton "$site_3_0.rad52" \
        -activebackground #d9d9d9 -activeforeground black -anchor w \
        -background #fdf7e7 -compound left -disabledforeground #a3a3a3 \
        -font "-family {Courier New} -size 10" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -justify left \
        -text "Radio" -variable "selectedFood" 
    vTcl:DefineAlias "$site_3_0.rad52" "radioFood02" vTcl:WidgetProc "frmCatering" 1
    radiobutton "$site_3_0.rad54" \
        -activebackground #d9d9d9 -activeforeground black -anchor w \
        -background #fdf7e7 -compound left -disabledforeground #a3a3a3 \
        -font "-family {Courier New} -size 10" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -justify left \
        -text "Radio" -variable "selectedFood" 
    vTcl:DefineAlias "$site_3_0.rad54" "radioFood03" vTcl:WidgetProc "frmCatering" 1
    radiobutton "$site_3_0.rad55" \
        -activebackground #d9d9d9 -activeforeground black -anchor w \
        -background #fdf7e7 -compound left -disabledforeground #a3a3a3 \
        -font "-family {Courier New} -size 10" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -justify left \
        -text "Radio" -variable "selectedFood" 
    vTcl:DefineAlias "$site_3_0.rad55" "radioFood04" vTcl:WidgetProc "frmCatering" 1
    radiobutton "$site_3_0.rad57" \
        -activebackground #d9d9d9 -activeforeground black -anchor w \
        -background #fdf7e7 -compound left -disabledforeground #a3a3a3 \
        -font "-family {Courier New} -size 10" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -justify left \
        -text "Radio" -variable "selectedFood" 
    vTcl:DefineAlias "$site_3_0.rad57" "radioFood05" vTcl:WidgetProc "frmCatering" 1
    place $site_3_0.rad47 \
        -in $site_3_0 -x 0 -relx 0.035 -y 0 -rely 0.061 -width 0 \
        -relwidth 0.905 -height 0 -relheight 0.115 -anchor nw \
        -bordermode ignore 
    place $site_3_0.rad52 \
        -in $site_3_0 -x 0 -relx 0.035 -y 0 -rely 0.242 -width 0 \
        -relwidth 0.905 -height 0 -relheight 0.115 -anchor nw \
        -bordermode ignore 
    place $site_3_0.rad54 \
        -in $site_3_0 -x 0 -relx 0.035 -y 0 -rely 0.424 -width 0 \
        -relwidth 0.905 -height 0 -relheight 0.115 -anchor nw \
        -bordermode ignore 
    place $site_3_0.rad55 \
        -in $site_3_0 -x 0 -relx 0.035 -y 0 -rely 0.606 -width 0 \
        -relwidth 0.905 -height 0 -relheight 0.115 -anchor nw \
        -bordermode ignore 
    place $site_3_0.rad57 \
        -in $site_3_0 -x 0 -relx 0.035 -y 0 -rely 0.788 -width 0 \
        -relwidth 0.905 -height 0 -relheight 0.115 -anchor nw \
        -bordermode ignore 
    label "$top.lab49" \
        -activebackground #d9d9d9 -activeforeground black -anchor w \
        -background #f5deb5 -compound left -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 12 -weight bold" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 \
        -text "Please Pay:" 
    vTcl:DefineAlias "$top.lab49" "Label3" vTcl:WidgetProc "frmCatering" 1
    frame "$top.fra49" \
        -borderwidth 2 -background #fdf7e7 -height 75 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -width 185 
    vTcl:DefineAlias "$top.fra49" "FramePayChoice" vTcl:WidgetProc "frmCatering" 1
    set site_3_0 $top.fra49
    radiobutton "$site_3_0.rad58" \
        -activebackground #d9d9d9 -activeforeground black -anchor w \
        -background #fdf7e7 -compound left -disabledforeground #a3a3a3 \
        -font "-family {Courier New} -size 10" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -justify left \
        -text "Pre-Pay" -variable "selectedPay" 
    vTcl:DefineAlias "$site_3_0.rad58" "radioPay01" vTcl:WidgetProc "frmCatering" 1
    radiobutton "$site_3_0.rad59" \
        -activebackground #d9d9d9 -activeforeground black -anchor w \
        -background #fdf7e7 -compound left -disabledforeground #a3a3a3 \
        -font "-family {Courier New} -size 10" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -justify left \
        -text "Pay upon Pickup" -variable "selectedPay" 
    vTcl:DefineAlias "$site_3_0.rad59" "radioPay02" vTcl:WidgetProc "frmCatering" 1
    place $site_3_0.rad58 \
        -in $site_3_0 -x 0 -relx 0.054 -y 0 -rely 0.133 -width 0 \
        -relwidth 0.854 -height 0 -relheight 0.253 -anchor nw \
        -bordermode ignore 
    place $site_3_0.rad59 \
        -in $site_3_0 -x 0 -relx 0.054 -y 0 -rely 0.533 -width 0 \
        -relwidth 0.854 -height 0 -relheight 0.253 -anchor nw \
        -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.but47 \
        -in $top -x 0 -relx 0.583 -y 0 -rely 0.778 -width 87 -relwidth 0 \
        -height 26 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but48 \
        -in $top -x 0 -relx 0.767 -y 0 -rely 0.778 -width 87 -relwidth 0 \
        -height 26 -relheight 0 -anchor nw -bordermode ignore 
    place $top.ent48 \
        -in $top -x 0 -relx 0.817 -y 0 -rely 0.489 -width 54 -relwidth 0 \
        -height 30 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab48 \
        -in $top -x 0 -relx 0.6 -y 0 -rely 0.467 -width 0 -relwidth 0.19 \
        -height 0 -relheight 0.113 -anchor nw -bordermode ignore 
    place $top.lab50 \
        -in $top -x 0 -relx 0.183 -y 0 -rely 0.022 -width 0 -relwidth 0.207 \
        -height 0 -relheight 0.069 -anchor nw -bordermode ignore 
    place $top.lab51 \
        -in $top -x 0 -relx 0.183 -y 0 -rely 0.089 -width 0 -relwidth 0.207 \
        -height 0 -relheight 0.069 -anchor nw -bordermode ignore 
    place $top.lab47 \
        -in $top -x 0 -relx 0.567 -y 0 -rely 0.022 -width 0 -relwidth 0.423 \
        -height 0 -relheight 0.402 -anchor nw -bordermode ignore 
    place $top.fra48 \
        -in $top -x 0 -relx 0.05 -y 0 -rely 0.178 -width 0 -relwidth 0.475 \
        -height 0 -relheight 0.367 -anchor nw -bordermode ignore 
    place $top.lab49 \
        -in $top -x 0 -relx 0.15 -y 0 -rely 0.867 -width 0 -relwidth 0.207 \
        -height 0 -relheight 0.069 -anchor nw -bordermode ignore 
    place $top.fra49 \
        -in $top -x 0 -relx 0.133 -y 0 -rely 0.6 -width 0 -relwidth 0.308 \
        -height 0 -relheight 0.167 -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

proc 36 {args} {return 1}


Window show .
set btop1 ""
if {$vTcl(borrow)} {
    set btop1 .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop1 $vTcl(tops)] != -1} {
        set btop1 .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop1
Window show .top1 $btop1
if {$vTcl(borrow)} {
    $btop1 configure -background plum
}
