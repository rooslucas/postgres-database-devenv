import functions as fn

# Create a todo list
fn.create_list('schoonmaken')
fn.add_item('schoonmaken', 1, "'stofzuigen'")
fn.add_item('schoonmaken', 2, "'dweilen'")
fn.add_item('schoonmaken', 3, "'afstoffen'")
fn.add_item('schoonmaken', 4, "'soppen'")

fn.view('schoonmaken')

fn.remove_item('schoonmaken', 3)
fn.remove_item('schoonmaken', 2)

fn.view('schoonmaken')

