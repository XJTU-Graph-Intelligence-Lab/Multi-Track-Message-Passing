import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--device', type=str, default='cuda', help='cuda or cpu')
# dataset args
# 'texas','wisconsin','cornell','washington'
# 'cora', 'citeseer', 'pubmed'
parser.add_argument('--dataset', type=str, default='cora')
parser.add_argument('--new_split', type=bool, default=False, help="If set to True, the self-generated split will be used")
parser.add_argument('--train_spilt', type=float, default=20, help='train split type [20,0.48, 0.6]')
parser.add_argument('--split_id', type=int, default=1, help="selected split")

# prior model args
parser.add_argument('-bb', '--backbone', type=str, default='GCN', help='The backbone model [GCN, GAT, APPNP].')
parser.add_argument('--start_epoch_p', type=int, default=10, help='prior modis start epoch')
parser.add_argument('--end_epoch_p', type=int, default=50, help='prior modis start epoch')
parser.add_argument('--proir_layers', type=int, default=2, help='prior model layers')
parser.add_argument('--pheads', type=int, default=2, help='prior GAT heads')
parser.add_argument('--pdr', type=float, default=0., help='prior dr')
parser.add_argument('--p_hidden', type=int, default=64, help='prior dr')
parser.add_argument('--alpha', type=float, default=0.1, help='The alpha value for APPNP (default: 0.1).')
parser.add_argument('--K', type=int, default=10, help='The K value for APPNP (default: 10).')

# prior training args
parser.add_argument('--plr', type=float, default=0.01)
parser.add_argument('--plw', type=float, default=0.5, help='prior model pseudo label weight')

# mutil-track training args
parser.add_argument('--lr', type=float, default=0.01)
parser.add_argument('--tblr', type=float, default=0.005)
parser.add_argument('--tbwd', type=float, default=1e-4)
parser.add_argument('--tpwd', type=float, default=5e-5)
parser.add_argument('--lw', type=float, default=0.5, help='mtgnn model pseudo label weight')

# mutil-track model args
parser.add_argument('--ipt_conv', type=str, default='base')
parser.add_argument('--fai1', type=float, default=0.5, help='attn loss weight')
parser.add_argument('--start_epoch', type=int, default=100, help='prior modis start epoch')
parser.add_argument('--end_epoch', type=int, default=300, help='prior modis start epoch')
parser.add_argument('--tau', type=float, default=1, help='attn temperature ')
parser.add_argument('--layer_num', type=int, default=16, help='track conv layer')
parser.add_argument('--n_heads', type=int, default=2, help='sender attention')
parser.add_argument('--a', type=float, default=0.9, help='track resudial param')
parser.add_argument('--dr', type=float, default=0.5, help='drop out rate')
parser.add_argument('--num_hidden', type=int, default=16)
parser.add_argument('--num_K', type=int, default=100)
parser.add_argument('--num_K_decay', type=int, default=30)

parser.add_argument('--num_epochs_patience', type=int, default=100)
parser.add_argument('--num_epochs_max', type=int, default=200)

parser.add_argument('--c_rounds', type=int, default=2)
parser.add_argument('--learning_rate_decay_patience', type=int, default=100)
parser.add_argument('--learning_rate_decay_factor', type=float, default=0.8)
args = parser.parse_args()