const archivedIcn = '<svg width="24" height="24" xmlns="http://www.w3.org/2000/svg" fill-rule="evenodd" clip-rule="evenodd"><path d="M18.546 1l5.454 6.986v15.014h-24v-15.014l5.477-6.986h13.069zm-5.546 14v-3h-2v3h-3l4 4 4-4h-3zm8.474-7l-3.906-5h-11.085l-3.951 5h18.942z"/></svg>';
const unarchivedIcn = '<svg width="24" height="24" xmlns="http://www.w3.org/2000/svg" fill-rule="evenodd" clip-rule="evenodd"><path d="M24 23h-24v-15.014l5.477-6.986h13.069l5.454 6.986v15.014zm-2-13h-20v11h20v-11zm-9 5h3l-4 4-4-4h3v-3h2v3zm4.568-12h-11.085l-3.951 5h18.942l-3.906-5z"/></svg>';
const replyIcn = 'data:image/png;base64,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';

document.addEventListener('DOMContentLoaded', function () {
	// getting last verision

	// Use buttons to toggle between views
	document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
	document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
	document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
	document.querySelector('#compose').addEventListener('click', () => compose_email());

	// check if submit button is clicked
	document.querySelector('form').onsubmit = () => {
		send_email();
		return false;
	}

	// By default, load the inbox
	load_mailbox('inbox');
});


function compose_email(recipients = '', subject = '', body = '') {

	// Show compose view and hide other views
	document.querySelector('#emails-view').style.display = 'none';
	document.querySelector('#compose-view').style.display = 'block';
	emailClear();

	// Clear out composition fields
	document.querySelector('#compose-recipients').value = recipients;
	document.querySelector('#compose-subject').value = subject;
	document.querySelector('#compose-body').value = body;
}

function load_mailbox(mailbox) {

	// push to the history
	// history.pushState({section: mailbox},"", `${mailbox}`)

	// Show the mailbox and hide other views
	document.querySelector('#emails-view').style.display = 'block';
	document.querySelector('#compose-view').style.display = 'none';
	emailClear();

	fetch(`emails/${mailbox}`, {
			method: 'GET'
		})
		.then(result => result.json())
		.then(response => {
			// console.log(response)
			let emailsView = document.querySelector('#emails-view');
			response.forEach(element => {
				// email
				let email = document.createElement('div');
				email.style.padding = '3px';
				email.addEventListener('click', () => {
					load_mail(element['id']);
				})

				if (element['read'] == true) {
					email.style.backgroundColor = '#B4B9BF';
				}
				email.classList.add('email');

				// sender
				let sender = document.createElement('span')
				sender.innerHTML = '<b>' + element['sender'] + '</b>';
				sender.style.float = 'left';
				email.appendChild(sender);

				// subject
				let subject = document.createElement('span');
				subject.innerHTML = element['subject'];
				subject.style.float = 'left';
				subject.style.marginLeft = '10px';
				email.appendChild(subject);

				// date
				let date = document.createElement('span');
				date.innerHTML = element['timestamp'];
				date.style.float = 'right';
				date.style.color = 'grey';
				email.appendChild(date);


				// add email
				emailsView.appendChild(email);
			});
		})

	// Show the mailbox name
	document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
}

// claer email div from any childs and hide
function emailClear() {
	let emailView = document.querySelector('#email-view');
	emailView.style.display = 'none';
	var child = emailView.lastChild;
	while (child) {
		emailView.removeChild(child);
		child = emailView.lastChild;
	}
}

// mark as read function
function mark_as_read(id) {
	fetch(`emails/${id}`, {
		method: 'PUT',
		body: JSON.stringify({
			read: true
		})
	})
}

// mark as archived
function archive(id) {
	fetch(`emails/${id}`, {
		method: "PUT",
		body: JSON.stringify({
			archived: true
		})
	})

}

// mark as unarchived
function unarchive(id) {
	fetch(`emails/${id}`, {
		method: "PUT",
		body: JSON.stringify({
			archived: false
		})
	})

}

function load_mail(id) {
	// Show compose view and hide other views
	document.querySelector('#email-view').style.display = 'block';
	document.querySelector('#emails-view').style.display = 'none';
	document.querySelector('#compose-view').style.display = 'none';


	fetch(`emails/${id}`, {
			method: "GET"
		})
		.then(result => result.json())
		.then(response => {

			// mark email as read
			mark_as_read(id);

			// get email-view div
			let emailView = document.querySelector('#email-view');

			// get subject (if any)
			if (response['subject']) {
				let subject = document.createElement('h1');
				subject.innerHTML = response['subject'];
				emailView.appendChild(subject);
			}


			// get email of sender
			let sender = document.createElement('h3');
			sender.innerHTML = response['sender'];
			sender.style.marginRight = '100px';
			emailView.appendChild(sender);

			// button for archive
			let archiveBtn = document.createElement('a');
			archiveBtn.href = '';
			if (response['archived']) {
				archiveBtn.onclick = () => {
					unarchive(response['id']);
				}
				archiveBtn.innerHTML = archivedIcn;
			} else {
				archiveBtn.onclick = () => {
					archive(response['id']);
				}
				archiveBtn.innerHTML = unarchivedIcn;
			}
			archiveBtn.style.marginLeft = '10px';
			sender.appendChild(archiveBtn);

			//button for replying
			let replyBtn = document.createElement('a');
			replyBtn.href = '';
			// icon for reply button
			let replyIcon = document.createElement('img');
			replyIcon.src = replyIcn;
			replyIcon.style.marginLeft = '10px';
			replyIcon.style.height = '20px';
			replyIcon.style.width = '20px';
			replyIcon.onclick = () => {
				const replyBody = `On ${response['timestamp']} ${response['sender']} wrote: ${response['body']} \n`;
				const replySubject = ( response['subject'].includes('Re: '))? response['subject'] : `Re: ${response['subject']}`;
				compose_email(response['sender'], replySubject, replyBody);
				return false;
			}
			replyBtn.appendChild(replyIcon);
			sender.appendChild(replyBtn);


			// breakline 
			emailView.appendChild(document.createElement('hr'));

			// get body of an email
			let body = document.createElement('p')
			body.innerHTML = response['body'];
			emailView.appendChild(body);
		})

}


function create_alert(result) {
	let alertDiv = document.createElement('div');
	// set alert style 'warning' or 'success'
	const alertClass = ('error' in result) ? "alert alert-warning" : "alert alert-success";
	alertDiv.className = alertClass + ' appear';

	// show message of result
	if ('error' in result) {
		alertDiv.innerHTML = result['error'];
	} else {
		alertDiv.innerHTML = result['message'];
	}

	document.querySelector('#alertDiv').appendChild(alertDiv);

	alertDiv.addEventListener('animationend', () => {
		alertDiv.className = alertClass + ' disappear';
		setTimeout(() => {
			alertDiv.style.animationPlayState = 'running';
			alertDiv.addEventListener('animationend', () => {
				alertDiv.remove()
			});
		}, 2000);

	})

}

function send_email() {
	// get data for sending mail
	const recipients = document.querySelector('#compose-recipients').value;
	const subject = document.querySelector('#compose-subject').value;
	const body = document.querySelector('#compose-body').value;

	fetch('/emails', {
			method: 'POST',
			body: JSON.stringify({
				recipients: recipients,
				subject: subject,
				body: body
			})
		})
		.then(response => response.json())
		.then(result => {
			// print result
			console.log(result)
			create_alert(result);
			if (!('error' in result))
				load_mailbox('sent')
		});
	return false;
}